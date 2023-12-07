from django.contrib import admin

from .models import CustomUser, UserDetail

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    list_display_links = ("id", "username")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserDetail)