from django.contrib import admin

from . import models as md


class PhotoUrlModelAdmin(admin.ModelAdmin):
    list_display = ('uri', 'created_at',)
    ordering = ('created_at',)


admin.site.register(md.PhotoUrl, PhotoUrlModelAdmin)
