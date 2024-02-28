from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contents']
    # fields = ['title', 'content'] # 이전 버전에서는 fields를 사용했습니다.

admin.site.register(Post, PostAdmin)