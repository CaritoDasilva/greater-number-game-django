from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.


def set_number(request):
    if int(request.session['magic_number']) <= 0:
        request.session['magic_number'] = str(random.randint(1, 100))
    print(request.session['magic_number'])
    return render(request, 'index.html')


def set_guess(request):
    magic_number = int(request.session['magic_number'])
    guess_number = int(request.POST['guess_number'])
    print(magic_number)
    print(guess_number)
    if magic_number == guess_number:
        request.session['result'] = 1
    elif magic_number > guess_number:
        request.session['result'] = 2
    elif magic_number < guess_number:
        request.session['result'] = 3
    return redirect('/')


def reset_game(request):
    request.session['magic_number'] = str(0)
    request.session['result'] = None
    return redirect('/')
