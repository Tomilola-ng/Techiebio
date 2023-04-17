import django_filters
from .models import Article
from django_filters import CharFilter


class ArticleFilter(django_filters.FilterSet):
    content = CharFilter(field_name="content", lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['content']