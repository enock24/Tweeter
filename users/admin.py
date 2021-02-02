from django.contrib import admin
from users.models import Tweet, Profile

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)

# class Meta:
#         verbose_name = 'Tweet'
#         verbose_name_plural = 'Tweets'