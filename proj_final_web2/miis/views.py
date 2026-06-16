from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Mii, Ilha
# Create your views here.

def painel_mii(request):
    miis = Mii.objects.all()
    return render(request, "painel/mii.html", {'miis':miis})

def painel_ilha(request):
    ilhas = Ilha.objects.all()
    return render(request, "painel/ilha.html", {'ilhas':ilhas})