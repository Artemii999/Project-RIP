from django.shortcuts import render
from .models import Article
from django.http import Http404, HttpResponseRedirect

def index(request):
    articles_list = Article.objects.all()
    return render(request, 'articles/list.html', {'articles_list': articles_list})


def detail(request, article_id):
    ############################
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {'article' : a})