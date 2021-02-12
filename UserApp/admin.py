from django.contrib import admin

# Register your models here.
from UserApp.models import UserProfile


class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'image_tag']
    list_filter = ['user', ]


admin.site.register(UserProfile, ProductAdmin)
