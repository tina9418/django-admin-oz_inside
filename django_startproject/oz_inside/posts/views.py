from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Article
from .forms import ArticleForm

def post_list(request) :
    posts = Article.objects.all()
    return render(request, 'posts/post_list.html',{'posts : posts'})

def post_create(request):
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commt=False)
            article.user = User.objects.first()
            article.save()
            return redirect('post_list')
    else:
        form = ArticleForm()
    return render(request, 'post/post_create.html', {'form':form})

def post_detail(request, pk) :
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'posts/post_detail.html', {'post':post})    
