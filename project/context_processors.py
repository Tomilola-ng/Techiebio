from django.db.models import Count
from core.models import Article

def most_viewed_bios(request):
    most_viewed_bios = Article.bio_obj.annotate(num_views=Count('view_count')).order_by('num_views')[:5]
    return {'most_viewed_bios': most_viewed_bios}

def get_top_startups(request):
    startups = Article.startup_obj.annotate(num_views=Count('view_count')).order_by('num_views')[:5]
    return {'top_startup': startups}
