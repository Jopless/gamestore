from django.shortcuts import render, get_object_or_404
from news.models import News

# Create your views here.


def news_index(request):
    news = News.objects.all().filter(is_published=True)
    context = {
        'news': news,
        'nav' : 'news'
    }
    return render(request, 'news/news.html', context)


def news_page(request, news_id):
    news_page = get_object_or_404(News, pk=news_id)
    context = {
        'news_page' : news_page
    }
    return render(request, 'news/news_single_page.html', context)