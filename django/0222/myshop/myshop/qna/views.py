from django.shortcuts import render

def qna_list(request):
    return render(request, 'qna/qna_list.html')


def qna_detail(request, id):
    context = {
        "id" : id
    }

    return render(request, 'qna/qna_detail.html', context)