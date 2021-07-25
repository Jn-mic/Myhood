from django.contrib import admin
from __future__ import unicode_literals
from .models import neighbourhood, Profile, Authorities, Health, Post

# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Profile)
admin.site.register(Authorities)
admin.site.register(Health)
admin.site.register(Post)