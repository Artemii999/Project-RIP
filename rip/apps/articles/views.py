from django.shortcuts import render, redirect
from .models import Articles11
from .forms import Task1Form
from django.http import Http404, HttpResponseRedirect, HttpResponse


def main(request):
    return render(request, 'home.html')


def list(request):
    list_books = Articles11.objects.all()
    return render(request, 'list.html', {'list_books': list_books})


def detail(request, article_id):
    ############################
    try:
        a = Articles11.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {'article' : a})


def hello(request):
    error = ''
    if request.method == 'POST':
        form = Task1Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('/articles')
        else:
            error = 'Форма неверная'

    form = Task1Form()
    context = {
        'form': form,
        'error': error,

    }
    return render(request, 'createbook.html', context)