from django.contrib import admin
from .models import UserMessage
# Register your models here.

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('center_number','center_mc','center_pr','center_mobile','address','modify_person','add_time')
    search_fields = ('center_number','center_mc','center_pr','center_mobile','address','modify_person','add_time')


admin.site.register(UserMessage, UserMessageAdmin)