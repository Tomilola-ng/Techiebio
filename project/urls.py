from django.contrib import admin
from django.urls import path, include
from .view import home, featured, advertise
from core.views import detail
from .sitemaps import ArticleSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'static': StaticViewSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('auth/', admin.site.urls),
    path('articles/', include('core.urls')),

    path('', home, name="home_view"), 

    path('featured/', featured, name='featured_view'),
    path('advertise/', advertise, name='advertise_view'),

    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('<slug:slug>/', detail.as_view(), name='detail_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
