from django.contrib import admin
from .models import Post,registration,Preference,Comment,Subcomment

# # Register your models here.
admin.site.register(Post)
admin.site.register(registration)
admin.site.register(Preference)
admin.site.register(Comment)
admin.site.register(Subcomment)
