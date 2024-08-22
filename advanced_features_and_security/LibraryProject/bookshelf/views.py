from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # Handle form submission to create a new article
        pass
    return render(request, 'article_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Handle form submission to edit the article
        pass
    return render(request, 'article_form.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article_confirm_delete.html', {'article': article})
