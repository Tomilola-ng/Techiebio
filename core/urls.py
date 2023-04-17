from django.urls import path 
from .views import detail, bioList, startList, list

 
urlpatterns = [
    path('', list, name='list_view'),
    path('bios', bioList, name='bio_list'),
    path('startups', startList, name='start_list'),
]