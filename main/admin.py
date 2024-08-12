from django.contrib import admin

from main.models import ShortedURL


class ShortedURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'short_url', 'death_time')


admin.site.register(ShortedURL, ShortedURLAdmin)
# Register your models here.
