from django.shortcuts import render
from .models import Articles


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})
