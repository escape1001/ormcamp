from django.contrib import admin
from .models import Post, Comment, Tag

admin.site.register([Post, Comment, Tag])