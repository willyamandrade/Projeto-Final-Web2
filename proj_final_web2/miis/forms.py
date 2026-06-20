from django import forms
from .models import Mii, Ilha

class MiiForm(forms.ModelForm):
    class Meta:
        model=Mii
        fields=('foto_mii', 'nome_mii', 'idade_mii', 'datadenascimento_mii','comidafavorita1_mii','comidafavorita2_mii','personalidade_mii','genero_mii','generoquegosta_mii','felicidade_mii')

        labels = {
            'foto_mii' : 'Foto',
            'nome_mii' : 'Nome',
            'idade_mii' : 'Idade',
            'datadenascimento_mii' : 'Data de Nascimento',
            'comidafavorita1_mii': 'Comida Favorita 01',
            'comidafavorita2_mii': 'Comida Favorita 02',
            'personalidade_mii': 'Personalidade',
            'genero_mii': 'Gênero',
            'generoquegosta_mii': 'Gênero que gosta',
            'felicidade_mii': 'Nível de Felicidade',
        }

        widgets = {
            'datadenascimento_mii' : forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

class MiiDetalheForm(forms.ModelForm):
    class Meta:
        model=Mii
        fields=('detalhes_mii',)

        labels={
            'detalhes_mii' : 'Detalhes',
        }

        widgets={
            'detalhes_mii' : forms.Textarea()
        }

class IlhaForm(forms.ModelForm):
    class Meta:
        model=Ilha
        fields=('nome_ilha',)

        labels = {
            'nome_ilha' : 'Nome da Ilha',
        }

        

