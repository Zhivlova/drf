from django.contrib import admin
from .models import User



@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('uid', 'first_name', 'last_name', 'email')
    list_display_links = ('first_name',)


