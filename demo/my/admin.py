from django.contrib import admin
from .models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'limit', 'status', 'address', 'start_time', 'create_time')
	list_display_links = ('name',)


class GuestAdmin(admin.ModelAdmin):
	list_display = ('id', 'realname', 'phone', 'email', 'sign', 'create_time', 'event')
	list_display_links = ('realname',)


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
