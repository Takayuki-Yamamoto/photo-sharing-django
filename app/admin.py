from django.contrib import admin

from . import models as md


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at',)
    ordering = ('created_at',)


admin.site.register(md.Photo, PhotoModelAdmin)
