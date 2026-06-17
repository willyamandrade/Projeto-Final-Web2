from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Mii, Ilha
from .forms import *
from accounts.models import Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def painel_mii(request):
    miis = Mii.objects.all()
    return render(request, "painel/mii.html", {'miis':miis})

@login_required
def painel_ilha(request):
    ilhas = Ilha.objects.all()
    return render(request, "painel/ilha.html", {'ilhas':ilhas})

@login_required
def add_mii(request):

    mydict={}
    form=MiiForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "painel/add_mii.html", {'form':form})

@login_required
def add_ilha(request):

    form=IlhaForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        ilha_legal = form.save(commit=False)
        ilha_legal.proprietario_ilha = Perfil.objects.get(user=request.user)
        ilha_legal.save()
        return redirect('')
    
    return render(request, "painel/add_ilha.html", {'form':form})

# @login_required
# def edit_mii(request):
#     miis = Mii.objects.all()
#     return render(request, "painel/mii.html", {'miis':miis})

# @login_required
# def edit_ilha(request):
#     ilhas = Ilha.objects.all()
#     return render(request, "painel/ilha.html", {'ilhas':ilhas})

# @login_required
# def del_mii(request):
#     miis = Mii.objects.all()
#     return render(request, "painel/mii.html", {'miis':miis})

# @login_required
# def del_ilha(request):
#     ilhas = Ilha.objects.all()
#     return render(request, "painel/ilha.html", {'ilhas':ilhas})