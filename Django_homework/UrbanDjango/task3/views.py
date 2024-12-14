from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.defaultfilters import title


# Create your views here.

def main(request):
    title = 'Главная страница'
    text = 'Главная страница магазина'

    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/main.html', context)

def games(request):
    title = 'Игры'
    text = 'Каталог игр'

    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/games.html', context)

def basket(request):
    title = 'Корзина'
    text = 'Игры в корзине'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/basket.html', context)


