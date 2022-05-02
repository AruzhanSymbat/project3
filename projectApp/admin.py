from django.contrib import admin

from .models import Feedback, Posts, Nature, User

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Posts)
admin.site.register(Nature)
admin.site.register(User)