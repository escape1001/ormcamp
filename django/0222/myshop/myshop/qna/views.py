from django.shortcuts import render, redirect
from .models import Question

def qna_list(request):
    questions = Question.objects.all().order_by("-id")
    context = {"question_list":questions}
    return render(request, 'qna/qna_list.html', context)


def qna_detail(request, id):
    question = Question.objects.get(id=id)
    context = {"question":question}

    return render(request, 'qna/qna_detail.html', context)


def qna_create(request, title):
    author = "user"
    contents = f"hello contents {title}"
    q = Question.objects.create(title=title, author=author, contents=contents)
    q.save()

    return redirect("qna_list")


def qna_delete(request, id):
    q = Question.objects.get(id=id)
    q.delete()

    return redirect("qna_list")