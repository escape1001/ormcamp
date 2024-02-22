from django.shortcuts import render
from .models import Question

def qna_list(request):
    questions = Question.objects.all()
    context = {"question_list":questions}
    return render(request, 'qna/qna_list.html', context)


def qna_detail(request, id):
    question = Question.objects.get(id=id)
    context = {"question":question}

    return render(request, 'qna/qna_detail.html', context)