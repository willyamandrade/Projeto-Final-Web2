from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_decode
from miis.models import *

def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            perfil = Perfil.objects.create(
                user=user,
                foto=form.cleaned_data['foto']
            )

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = f"http://localhost:8000/ativar/{uid}/{token}/"

            nome_user = User.objects.get(pk=urlsafe_base64_decode(uid).decode()).username
            send_mail('Ative sua conta: ', f'Clique aqui: {link}', 'web2@ifce.edu.br', [user.email])
            
            return render(request, 'accounts/cadastro_sucesso.html', {})
    else:
        form = CadastroForm()
    return render(request, 'accounts/cadastrar.html', {'form': form})
    
def ativar_conta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        perfil = user.perfil
        perfil.email_confirmado = True
        perfil.save()
        return redirect('login')
    else:
        return render(request, 'accounts/token_invalido.html')