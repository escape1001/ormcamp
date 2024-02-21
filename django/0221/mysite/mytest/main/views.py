from django.shortcuts import render
from django.http import HttpResponse

blog_list = [
    {
        "id": 1,
        "title": "Blog 1",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "Blog 2",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "Blog 3",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list = [
    {
        "id": 1,
        "username": "hojun",
        "email": "hojun@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]


def index(request):
    return HttpResponse("index 페이지입니다.")

def bloglist(request):
    context = {"blog_list":blog_list}

    return render(request, 'main/blog.html', context)

def blogdetails(request, pk):
    blog_item = [i for i in blog_list if i["id"] == pk][0]

    return HttpResponse(f'''
        <h1>{blog_item["id"]} / {blog_item["title"]}</h1>
        <div>
            {blog_item["content"]}
        </div>
        <p>
            by. {blog_item["author"]}
        </p>
    ''')

def userdetails(request, user):
    find_user = None

    for i in user_list :
        if i["username"] == user :
            find_user = i

    if find_user is None :
        return HttpResponse(f"등록되지 않은 유저입니다.")
    
    return HttpResponse(f"userdetails : {user} 페이지입니다.")