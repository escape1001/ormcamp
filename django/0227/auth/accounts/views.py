from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# CBV 방식으로 구현. (추상화 강도 높음)
signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/form.html",
    success_url=settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name="accounts/form.html",
    # success_url=settings.LOGIN_REDIRECT_URL,
    # next_page=settings.LOGIN_REDIRECT_URL,
)

logout = LogoutView.as_view(
    next_page=settings.LOGIN_URL,
)

@login_required
def profile(request):
    context = {}
    return render(request, 'accounts/profile.html', context)

def logincheck(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/login_check.html')
    else :
        return HttpResponse("로그인 안됨")
    
# fbv로 로그인 구현하기
def loginfbv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login 성공")
        else:
            return HttpResponse("login 실패")
    return render(request, 'accounts/loginfbv.html')


# def signup(request):
#     context = {}
#     return render(request, 'accounts/signup.html', context)

# def login(request):
#     context = {}
#     return render(request, 'accounts/login.html', context)

# def logout(request):
#     context = {}
#     return render(request, 'accounts/logout.html', context)