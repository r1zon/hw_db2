from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Themes, ArticleTheme


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().prefetch_related('themes')
    theme_list = ArticleTheme.objects.all().prefetch_related('article')
    context = {'object_list': object_list,
               'theme_list': theme_list,
               }
    # article.scopes.all
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    return render(request, template, context)
