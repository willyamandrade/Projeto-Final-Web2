from django import forms
from .models import Mii, Ilha

class MiiForm(forms.ModelForm):
    class Meta:
        model=Mii
        fields='__all__'

        labels = {
            'nome_mii' : 'Nome',
            'idade_mii' : 'Idade',
            'datadenascimento_mii' : 'Data de Nascimento',
            'comidafavorita1_mii': 'Comida Favorita 01',
            'comidafavorita2_mii': 'Comida Favorita 02',
            'personalidade_mii': 'Personalidade',
            'genero_mii': 'Gênero',
            'generoquegosta_mii': 'Gênero que gosta',
            'felicidade_mii': 'Nível de Felicidade',
            'ilha_mii' : 'Mora em',
        }



class IlhaForm(forms.ModelForm):
    class Meta:
        model=Ilha
        fields=('nome_ilha',)

        labels = {
            'nome_ilha' : 'Nome da Ilha',
        }

        

