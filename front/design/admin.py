# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class RegisterAdmin(admin.ModelAdmin):

    list_display = (
        'imageRegister',
        'nom',
        'user',
        'email',
        'contact',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    def imageRegister(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Register, RegisterAdmin)
