from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class CadastroForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Endereço de e-mail')
    senha = forms.CharField(widget=forms.PasswordInput)
    foto = forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username', 'email')
        
        def __init__(self, *args, **kwargs):
            super(CadastroForm, self).__init__(*args, **kwargs)

            for fieldname in ['username', 'email', 'password']:
                self.fields['username'].help_text = None


        widget = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha'])
        if commit:
            user.save()
        return user
    
print(CadastroForm)