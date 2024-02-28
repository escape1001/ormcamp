from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView


signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = "accounts/accounts_form.html",
    success_url = settings.LOGIN_URL
)

login = LoginView.as_view(
    template_name = "accounts/accounts_form.html",
)

logout = LogoutView.as_view(
    next_page=settings.LOGIN_REDIRECT_URL,
)

@login_required # 로그인 된 경우에만 접근 가능
def profile(request):
    return render(request, 'accounts/profile.html')