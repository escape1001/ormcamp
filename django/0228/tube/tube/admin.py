from django.contrib import admin
from .models import Video, Comment, Like, Tag

admin.site.register([Video, Comment, Like, Tag])