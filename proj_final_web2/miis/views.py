from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Mii, Ilha
from .forms import *
from accounts.models import Perfil
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required # <-- IMPEDE acesso de usuários não logados
def home(request):
    
    if not request.user.perfil.email_confirmado:
        messages.error(request, 'Opsss, sua conta ainda não foi confirmada!')
        return redirect('login')
    
    id_user = request.user.perfil.id
    ilhas = Ilha.objects.filter(proprietario_ilha_id=id_user)
    qtd_mii = 0
    
    # itera por cada ilha do usuário, contando o número de miis que o pertencem 
    for ilha in ilhas:
        ilha_do_usuario = Mii.objects.filter(ilha_mii=ilha)
        qtd_mii += ilha_do_usuario.count()

    return render(request, 'principal/home.html', {'ilhas':ilhas, 'qtd_mii' : qtd_mii})

@login_required
def painel_mii(request, ilha_id):

    miis = Mii.objects.filter(ilha_mii=ilha_id)
    
    return render(request, "painel/mii.html", {'miis' : miis, 'ilha_id' : ilha_id})

@login_required
def painel_ilha(request):

    id_user = request.user.perfil.id
    ilhas = Ilha.objects.filter(proprietario_ilha_id=id_user)

    return render(request, "painel/ilha.html", {'ilhas':ilhas})

@login_required
def add_mii(request, ilha_id):

    form=MiiForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        mii_legal = form.save(commit=False)
        mii_legal.ilha_mii = Ilha.objects.get(pk=ilha_id)
        mii_legal.save()

        return redirect('painelmii', ilha_id)

    return render(request, "painel/add_mii.html", {'form':form, 'ilha_id' : ilha_id})

@login_required
def add_ilha(request):

    form=IlhaForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        ilha_legal = form.save(commit=False)
        ilha_legal.proprietario_ilha = Perfil.objects.get(user=request.user)
        ilha_legal.save()
        return redirect('painelilha')
    
    return render(request, "painel/add_ilha.html", {'form':form})

@login_required
def edit_mii(request, ilha_id, id):

    mii_editar = Mii.objects.get(pk=id)
    form=MiiForm(request.POST or None,request.FILES or None, instance=mii_editar)

    if form.is_valid():
        form.save()
        return redirect('painelmii', ilha_id)

    return render(request, "painel/edit_mii.html", {'form':form, 'ilha_id' : ilha_id})

@login_required
def edit_ilha(request, id):

    ilha_editar = Ilha.objects.get(pk=id)
    form=IlhaForm(request.POST or None,request.FILES or None, instance=ilha_editar)
    
    if form.is_valid():
        ilha_legal = form.save(commit=False)
        ilha_legal.proprietario_ilha = Perfil.objects.get(user=request.user)
        ilha_legal.save()
        return redirect('painelilha')
    
    return render(request, "painel/edit_ilha.html", {'form':form})

@login_required
def del_mii(request, ilha_id, id):

    mii_deletar = Mii.objects.get(pk=id)

    if request.method=="POST":
        mii_deletar.delete()
        return redirect('painelmii', ilha_id)
    
    return render(request, 'painel/del_mii.html', {'mii' : mii_deletar, 'ilha_id' : ilha_id})

@login_required
def del_ilha(request, id):

    ilha_deletar = Ilha.objects.get(pk=id)

    if request.method=="POST":
        ilha_deletar.delete()
        return redirect('painelilha')
    
    return render(request, 'painel/del_ilha.html', {'ilha' : ilha_deletar})