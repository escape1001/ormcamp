from django.shortcuts import render

def qna_list(request):
    return render(request, 'qna/index.html')

def qna_detail(request, id):
    return render(request, 'qna/qna_detail.html', {"id":id})