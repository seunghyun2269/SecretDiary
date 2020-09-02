from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def diary(request):
    return render(request, 'diary.html')

def create(request):
    return render(request, 'create.html')

def board(request):
    return render(request, 'board.html')