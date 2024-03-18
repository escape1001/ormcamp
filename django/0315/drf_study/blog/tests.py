from django.test import TestCase, Client
from rest_framework.test import APIClient
from .models import Post
from django.contrib.auth.models import User


class TestBlog(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='test',
            password='test1234!'
        )
        self.user.save()
        
        self.post_001 = Post.objects.create(
            title ='test post 1',
            content ='test post 111111',
            author = self.user,
        )
        self.post_001.save()

    # 회원 게시판 /blog : 회원인 사람만 R, C 가능
    def test_blog_list(self):
        print("blog list 테스트 시작")
        print(">> 비회원 읽기 테스트")
        response = self.client.get('/blog/post/')
        self.assertEqual(response.status_code, 403)
        
        print(">> 회원 읽기 테스트")
        self.client.login(
            username='test',
            password='test1234!'
        )
        response = self.client.get('/blog/post/')
        self.assertEqual(response.status_code, 200)
        print("blog list 테스트 END ---------")

    # 회원 게시물 상세보기 /blog/int:post_pk: 회원인 사람만 R, 작성자만 UD 가능
    def test_blog_detail_read(self):
        print("blog detail - read 테스트 시작")
        print(">> 비회원 읽기 테스트")
        response = self.client.get('/blog/post/1')
        self.assertEqual(response.status_code, 403)
        
        print(">> 회원 읽기 테스트")
        self.client.login(
            username='test',
            password='test1234!'
        )
        response = self.client.get('/blog/post/1')
        self.assertEqual(response.status_code, 200)
        print("notice detail - read 테스트 END ---------")

    # 회원 게시물 작성 /blog/int:post_pk: 회원인 사람만 R, 작성자만 UD 가능
    def test_blog_detail_create(self):
        print("blog detail - create 테스트 시작")
        print(">> 비회원 작성 테스트")
        response = self.client.post(
            "/blog/post/",
            {
                "title":"test post 2",
                "content":"test post 22222",
                "author":self.user.id,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 403)
        
        print(">> 회원 작성 테스트")
        self.client.login(
            username='test',
            password='test1234!'
        )
        response = self.client.post(
            "/blog/post/",
            {
                "title":"test post 2",
                "content":"test post 22222",
                "author":self.user.id,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 201)
        posts = Post.objects.all()
        for i in posts:
            print(i.title)
        print("notice detail - create 테스트 END ---------")

    # 자유 게시판 /notice : 회원이 아닌 사람도 R 가능, 회원인 사람만 
    # 자유 게시물 상세보기 /notice/int:post_pk: 회원이 아닌 사람도 R 가능, 작성자만 UD 가능
    