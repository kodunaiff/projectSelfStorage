from django.contrib import admin

from .models import Storehouse, Box, UserProfile, StorehouseImage


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Storehouse)
class StorehouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass



@admin.register(StorehouseImage)
class StorehouseImageAdmin(admin.ModelAdmin):
    list_display = ['storehouse', 'number_pic', 'img']
    raw_id_fields = ['storehouse']
