from django import forms
from .models import Mii, Ilha

class MiiForm(forms.ModelForm):
    datadenascimento_mii = forms.DateField(
        label='Data de Nascimento', 
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model=Mii
        fields=('nome_mii', 'idade_mii', 'datadenascimento_mii','comidafavorita1_mii','comidafavorita2_mii','personalidade_mii','genero_mii','generoquegosta_mii','felicidade_mii')

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
        }



class IlhaForm(forms.ModelForm):
    class Meta:
        model=Ilha
        fields=('nome_ilha',)

        labels = {
            'nome_ilha' : 'Nome da Ilha',
        }

        

