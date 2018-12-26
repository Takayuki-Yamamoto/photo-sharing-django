from django.contrib import admin

from . import models as md


class PhotoUrlModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'uri' 'created_at',)
    ordering = ('id')


admin.site.register(md.PhotoUrl, PhotoUrlModelAdmin)
