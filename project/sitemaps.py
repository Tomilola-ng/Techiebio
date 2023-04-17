from django.contrib.sitemaps import Sitemap
from core.models import Article
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['advertise_view', 'featured_view', 'start_list', 'bio_list']
    def location(self, item):
        return reverse(item)

class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.all()
    # def location(self, item):
    #     return reverse(item)
    # def location(self, obj: Model) -> str:
        # return super().location(obj)()