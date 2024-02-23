from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} / {self.title} / {self.author}"