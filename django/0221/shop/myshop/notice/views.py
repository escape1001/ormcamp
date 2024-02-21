from django.shortcuts import render

def notice_main(request):
    return render(request, 'notice/index.html')

def free_board(request):
    return render(request, 'notice/free_board.html')

def free_board_detail(request, id):
    return render(request, 'notice/free_board_detail.html', {"id":id})

def onenone(request):
    return render(request, 'notice/onenone.html')

def onenone_detail(request, id):
    return render(request, 'notice/onenone_detail.html', {"id":id})