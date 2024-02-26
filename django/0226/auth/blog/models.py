from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)
    '''
        위처럼 할 수도 있고 upload_to를 아래처럼 함수로 지정할 수도 있음

        def get_image_path(instance, filename):
            return f"blog/{instance.pk}/%Y/%m/{filename}"
        main_image = models.ImageField(upload_to=get_image_path, blank=True)

        [폴더트리 깊게 파는 이유 : 탐색성능 이슈]
        # 이미지 중복되면 이미지에는 난수 들어가니 걱정하시지 않으셔도 됩니다.
        # 이미지가 하나의 폴더에 많아졌을 경우, 성능이슈가 있을 수 있습니다. 그래서 폴더 분리를 권장합니다.
        # 아니면 filename에 날짜를 넣는 것도 좋은 방법입니다.
        # 난수로 처리하면 보안성은 올라가지만 파일명을 알 수 없어서 관리가 어려울 수 있습니다.
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
