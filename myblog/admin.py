from django.contrib import admin
from .models import Contact

# Register your models here.

# @admin.register(Contact)
admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

