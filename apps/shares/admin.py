from django.contrib import admin
from .models import Share, ShareRecord, ShareGroup

admin.site.register(Share)
admin.site.register(ShareRecord)
admin.site.register(ShareGroup)
