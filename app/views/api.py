import os, tempfile
from django.http import HttpResponse, HttpResponseForbidden

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            ImageMessage, )

from cloudinary.uploader import upload
# from cloudinary.utils import cloudinary_url, private_download_url
from config.settings import CHANNEL_ACCESS_TOKEN, LINE_ACCESS_SECRET
from app.models import PhotoUrl

line_bot_api = LineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(channel_secret=LINE_ACCESS_SECRET)


def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()

    return HttpResponse('OK', status=200)


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='reply_message')
    )


@handler.add(MessageEvent, message=[ImageMessage])
def handle_image_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='invalid message')
        )
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(prefix=ext + '-', delete=True) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)

        upload_result = upload(tf.name, type="private")

        if "error" in upload_result:
            error_text = 'invalid image'
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=error_text)
            )
            return

        PhotoUrl.objects.create(cloud_id=upload_result['public_id'])
        # private_download_url(upload_result['public_id'], format=ext)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='save image')
        )
