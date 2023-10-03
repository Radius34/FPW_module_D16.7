from django.contrib import admin
from .models import Bulletin
from .utils import send_newsletter


admin.site.register(Bulletin)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        send_newsletter(obj.subject, obj.message)

