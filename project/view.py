from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from core.models import Article

def home(request):

    context = {
        'Bios': Article.bio_obj.all()[:6],
        'Startups': Article.startup_obj.all()[:6]
    }
    return render(request, 'home.html', context)

def featured(request):
    return render(request, 'featured.html')

def advertise(request):
    return render(request, 'advertise.html')