from django.contrib import admin

from .models import Event, Experience, User, Authenticator

admin.site.register(Event)
admin.site.register(Experience)
admin.site.register(User)
admin.site.register(Authenticator) # need to remove later