from django.test import TestCase, Client
from rest_framework.test import APIClient
from .models import Post
from accounts.models import CustomUser


class TestBlog(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(
            email='test@test.com',
            password='test1234!'
        )
        self.user.save()

        self.user2 = CustomUser.objects.create_user(
            email='test2@test.com',
            password='test1234!'
        )
        self.user2.save()
        
        self.post_001 = Post.objects.create(
            title ='test post 1',
            content ='test post 111111',
            author = self.user,
        )
        self.post_001.save()

    # 전체목록 조회 - 비회원 401 / 회원 200
    def test_blog_list(self):
        print("blog list 테스트 시작")
        print(">> 비회원 읽기 테스트")
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 401)
        
        print(">> 회원 읽기 테스트")
        self.client.force_authenticate(user=self.user)
        self.user.save()
        # self.client.login(email='test@test.com', password='test1234!')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        print("blog list 테스트 END ---------")


    # 글 상세보기 - 비회원 401 / 회원 200
    def test_blog_detail(self):
        print("blog detail 테스트 시작")
        print(">> 비회원 상세읽기 테스트")
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 401)

        print(">> 회원 상세읽기 테스트")
        self.client.force_authenticate(user=self.user)
        self.user.save()
        # self.client.login(email='test@test.com', password='test1234!')
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)


    # 글CUD - 비회원 401
    def test_blog_cud_nomember(self):
        print("blog 비회원 CUD 테스트 시작")
        print(">> 비회원 쓰기 테스트")
        response = self.client.post("/blog/", {
                "title" : "작성 테스트",
                "content" : "작성 테스트,,,,,",
                "author" : self.user.pk,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 401)

        print(">> 비회원 수정 테스트")
        response = self.client.put("/blog/1/", {
                "title" : "수정 테스트",
                "content" : "수정 테스트,,,,,",
            },
            format="json"
        )
        self.assertEqual(response.status_code, 401)

        print(">> 비회원 삭제 테스트")
        response = self.client.delete("/blog/1/")
        self.assertEqual(response.status_code, 401)


    # 글CUD - 회원
    def test_blog_cud_member(self):
        print("blog CUD 테스트 시작")
        print(">> 회원 쓰기 테스트")
        self.client.force_authenticate(user=self.user)
        self.user.save()
        # self.client.login(email='test@test.com', password='test1234!')
        response = self.client.post("/blog/", {
                "title" : "작성 테스트",
                "content" : "작성 테스트,,,,,",
                "author" : self.user.pk,
            },
            format="json"
        )
        post_id = response.data['id']
        print(f"post_id : {post_id}")
        self.assertEqual(response.status_code, 201)

        print(">> 회원타인 수정 테스트")
        self.client.force_authenticate(user=self.user2)
        self.user2.save()
        # self.client.logout()
        # self.client.login(email='test2@test.com', password='test1234!')
        response = self.client.put(f"/blog/{post_id}/", {
                "title" : "수정 테스트",
                "content" : "수정 테스트,,,,,",
                "author" : self.user.pk,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 403)

        print(">> 회원타인 삭제 테스트")
        response = self.client.delete(f"/blog/{post_id}/")
        self.assertEqual(response.status_code, 403)

        print(">> 회원본인 수정 테스트")
        self.client.force_authenticate(user=self.user)
        self.user.save()
        # self.client.logout()
        # self.client.login(email='test@test.com', password='test1234!')
        response = self.client.put(f"/blog/{post_id}/", {
                "title" : "수정 테스트",
                "content" : "수정 테스트,,,,,",
                "author" : self.user.pk,
            },
            format="json"
        )
        print("response")
        print(response)
        self.assertEqual(response.status_code, 200)

        print(">> 회원본인 삭제 테스트")
        response = self.client.delete(f"/blog/{post_id}/")
        self.assertEqual(response.status_code, 204)