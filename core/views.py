from django.shortcuts import render
from .models import Article
from hitcount.views import HitCountDetailView
from django.views.generic import DetailView, ListView, View
from django.contrib import messages
from django.db.models import Q
from .filters import ArticleFilter

def list(request):
    articles = Article.objects.all()
    myFilter = ArticleFilter(request.GET, queryset=articles)

    context = {
        'myFilter': myFilter,
    }

    return render(request, 'list.html', context)

def bioList(request):
    articles = Article.bio_obj.all()
    myFilter = ArticleFilter(request.GET, queryset=articles)

    context = {
        'myFilter': myFilter,
    }

    return render(request, 'list.html', context)

def startList(request):
    articles = Article.startup_obj.all()
    myFilter = ArticleFilter(request.GET, queryset=articles)

    context = {
        'myFilter': myFilter,
    }

    return render(request, 'list.html', context)

class detail(HitCountDetailView):
    model = Article
    count_hit = True
    context_object_name = 'article'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.object.tags.all().values_list('name', flat=True)
        context['meta_keywords'] = ', '.join(tags)
        return context