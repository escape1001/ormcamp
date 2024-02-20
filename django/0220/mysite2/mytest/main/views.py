from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return HttpResponse("<h1>index 메인화면입니다.</h1>")

def notice(request) :
    return HttpResponse("<h1>notice 화면입니다.</h1>")

def notice_detail(request, id) :
    return HttpResponse(f"<h1>notice detail : {id} 화면입니다.</h1>")

def contact(request) :
    return HttpResponse("<h1>contact 화면입니다.</h1>")

def abcd(request) :
    return HttpResponse("<h1>abcd 화면입니다.</h1>")

def user(request, username) :
    user_list = ["mini", "micky"]

    if username in user_list :
        return HttpResponse(f"<h1>안녕하세요! {username}님.</h1>")
    else :
        return HttpResponse(f"<h1>가입되지 않은 유저입니다. 회원가입을 하시겠습니까?</h1>")