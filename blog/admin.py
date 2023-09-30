from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username',)
    raw_id_fields = ('talked_operator',)

