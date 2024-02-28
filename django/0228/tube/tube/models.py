from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    thumbnail_image = models.ImageField(
        upload_to="tube/images/%Y/%m/%d/", blank=True
    )
    video_upload = models.FileField(
        upload_to="tube/images/%Y/%m/%d/", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='comments'
    )
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.contents


class Like(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='likes'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.video} / {self.author}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name