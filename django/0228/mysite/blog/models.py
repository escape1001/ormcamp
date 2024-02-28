from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE # user 삭제되면 글도 삭제됨
    )
    # N:M 관계를 만들어줍니다. 어디서든 정의해도 상관 없습니다.
    tags = models.ManyToManyField('Tag', blank=True)
    

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # related_name은 Post에서 Comment를 부를 때 사용할 이름
    # 만약 이름을 licat이라 바꾸면 템플릿 문법에서 아래와 같이 호출됩니다.
    # {% for comment in post.licat.all %}
    # ForeignKey는 1:N 관계를 만들어줍니다. 단, N에서 정의합니다.
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments' # 게시글 지워지면 덧글 지워짐
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE # 유저 지워지면 덧글 지워짐
    )

    def __str__(self):
        return self.message
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name