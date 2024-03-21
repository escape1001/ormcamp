from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import CustomUser
from .models import Notice

class NoticeTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(
            email='test@test.com',
            password='test1234!',
        )
        self.user.save()

        self.user2 = CustomUser.objects.create_user(
            email='test2@test.com',
            password='test1234!',
        )
        self.user2.save()

        self.notice_001 = Notice.objects.create(
            title="notice 001",
            content="notice 001111",
            author=self.user,
        )
        self.notice_001.save()


    # 공지 리스트 읽기 / 비회원 200, 회원 200
    def test_notice_list(self):
        print("notice list 테스트 시작")
        print(">> 비회원 읽기 테스트") 
        response = self.client.get('/notice/')
        self.assertEqual(response.status_code, 200)

        # 비회원이 200이면 회원도 200이므로 회원 테스트 생략


    # 공지 상세 읽기 / 비회원 200, 회원 200
    def test_notice_detail(self):
        print("notice detail 테스트 시작")
        print(">> 비회원 상세읽기 테스트") 
        response = self.client.get('/notice/1/')
        self.assertEqual(response.status_code, 200)

        # 비회원이 200이면 회원도 200이므로 회원 테스트 생략


    # 공지 CUD / 비회원 401 403 403
    def test_notice_nomember(self):
        print("notice CUD 테스트 시작")
        print(">> 비회원 create 테스트") 
        response = self.client.post('/notice/',{
                "title":"수정테스트",
                "content":"수정테스트222",
                "author":self.user.pk,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 401)

        print(">> 비회원 update 테스트") 
        response = self.client.put('/notice/1/',{
                "title":"수정테스트",
                "content":"수정테스트222",
                "author":self.user.pk,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 403)

        print(">> 비회원 delete 테스트") 
        response = self.client.delete('/notice/1/')
        self.assertEqual(response.status_code, 403)


    # 공지 CUD / 회원본인 201 200 204 / 회원타인 403 403 403
    def test_notice_nomember(self):
        print("notice CUD 테스트 시작")
        print(">> 회원 create 테스트") 
        self.client.force_authenticate(user=self.user)
        self.user.save()
        response = self.client.post('/notice/',{
                "title":"수정테스트",
                "content":"수정테스트222",
                "author":self.user.pk,
            },
            format="json"
        )
        print("create response")
        print(response.data)
        post_id = response.data['id']
        self.assertEqual(response.status_code, 201)

        print(">> 회원타인 update 테스트")
        self.client.force_authenticate(user=self.user2)
        self.user2.save()
        response = self.client.put(f'/notice/{post_id}/',{
                "title":"수정테스트",
                "content":"수정테스트222",
                "author":self.user.pk,
            },
            format="json"
        )
        self.assertEqual(response.status_code, 403)

        print(">> 회원타인 delete 테스트") 
        response = self.client.delete(f'/notice/{post_id}/')
        self.assertEqual(response.status_code, 403)

        print(">> 회원본인 update 테스트")
        self.client.force_authenticate(user=self.user)
        self.user.save()
        response = self.client.put(f'/notice/{post_id}/',{
                "title":"수정테스트",
                "content":"수정테스트222",
                "author":self.user.pk,
            },
            format="json"
        )
        print("update response")
        print(response.data)
        self.assertEqual(response.status_code, 200)

        print(">> 회원타인 delete 테스트") 
        response = self.client.delete(f'/notice/{post_id}/')
        self.assertEqual(response.status_code, 204)