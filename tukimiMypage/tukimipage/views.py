from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm

#デフォルトページ
def default(request):
    return render(request, 'tukimipage/default.html')

#プログラミング一覧ページ
def programlist(request):
    return render(request, 'tukimipage/programList.html')

#デフォルト関数
def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': '掲示板',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'tukimipage/index.html', context)

#詳細ページ関数
def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context ={
        'massage': 'show Article' + str(id),
        'article': article,
    }
    return render(request, 'tukimipage/detail.html',context)

#新規作成ページ関数
def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'tukimipage/new.html', context)

#編集ページ関数
def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)

    context = {
        'message': 'Edit Article',
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'tukimipage/edit.html', context)

#アップデートページ関数
def update(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()

    context = {
        'message': 'Update article ' + str(id),
        'article': article,
    }
    return render(request, 'tukimipage/detail.html', context)

#作成ページ関数
def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()

    context = {
        'message': 'Create article ' + str(article.id),
        'article': article,
    }
    return render(request, 'tukimipage/detail.html', context)

#削除ページ関数
def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'tukimipage/index.html', context)