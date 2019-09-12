from django.shortcuts import render
from news.models import News

# Create your views here.

def news_index(request):
    # news = News.objects.all().filter(is_published=True)
    # context = {
    #     'news': news
    # }
    return render(request, 'news/news.html')


