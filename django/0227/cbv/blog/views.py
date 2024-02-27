from django.db.models.query import QuerySet
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.db.models import Q

# 클래스 기반 뷰 != 제네릭 뷰
# 클래스로 HttpResponse를 리턴하면 그것도 클래스 기반 뷰라고 볼 수 있음
# 실무에서는 클래스 기반 뷰를 제네릭 뷰라고 혼용해서 많이 부름
# 제네릭 뷰 : 장고에서 제공하는 여러 기능을 미리 구현해놓은 클래스 기반 뷰

class PostList(ListView):
    model = Post
    ordering = "-pk" # 내림차순 정렬을 하겠다~
    # template_name = "blog/파일명.html" # 기본값 : blog/post_list.html

    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q', '')

        if q :
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(contents__icontains=q)
            ).distinct()

        return queryset
    

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    # fields = ['title', 'content', 'image']
    # template_name = "blog/파일명.html" # 기본값 : blog/post_form.html
    success_url = reverse_lazy("blog_list")
    ''' reverse_lazy 사용 이유 :
        object생성 후에 url로 이동해야 하는데 reverse는 함수이기 때문에 함수 실행 시점에 url로 이동해버림.
        post 생성 후에 url로 이동해야 하므로 lazy 걸어줌
    '''

class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    # fields = ["title", "content", "image"]
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html    
    # success_url = reverse_lazy("blog_list")

    def get_success_url(self):
        return reverse('blog_detail', args=[str(self.object.pk)])
    
    '''
    success_url = reverse_lazy("blog_list") : 정적인 페이지로 보낼 때. 상세 페이지로는 못감.
    def get_success_url : 동적인 페이지로 보낼 수 있음
    '''
    

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("blog_list")

class PostTest(CreateView):
    model = Post

    def get(self, request):
        return HttpResponse("get 요청이 왔습니다.")

    def post(self, request):
        return HttpResponse("post 요청이 왔습니다.")


# 실무에서는 urls.py에서 바로 as_view() 붙여서 사용.
# views.PostList.as_view() 요런식으로
blog_list = PostList.as_view()
blog_detail = PostDetail.as_view()
blog_write = PostCreate.as_view()
blog_edit = PostUpdate.as_view() 
blog_delete = PostDelete.as_view()
test = PostTest.as_view()


'''
Django에서 ListView와 같은 일반적인 Class-Based Views (CBV)를 사용할 때, 템플릿 이름은 기본적으로 다음과 같은 규칙을 따라 자동으로 생성됩니다.

PostList (ListView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_list.html
여기서의 기본 템플릿: <app_name>/post_list.html
템플릿 접근 방법:
{% for post in object_list %}
    {{ post.title }}
{% endfor %}


PostDetail (DetailView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_detail.html
여기서의 기본 템플릿: <app_name>/post_detail.html
템플릿 접근 방법: 
{{ object.title }}


PostCreate (CreateView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_form.html
여기서의 기본 템플릿: <app_name>/post_form.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>


PostUpdate (UpdateView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_form.html
여기서의 기본 템플릿: <app_name>/post_form.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>


PostDelete (DeleteView)
템플릿 이름 규칙:  <app_name>/<model_name_소문자>_confirm_delete.html
여기서의 기본 템플릿: <app_name>/post_confirm_delete.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    Are you sure you want to delete "{{ object.title }}"?
    <button type="submit">Delete</button>
</form>


* CreateView와 UpdateView는 같은 템플릿 이름 규칙을 사용합니다. 그래서 둘 다 _form.html을 기본으로 사용합니다.

'''