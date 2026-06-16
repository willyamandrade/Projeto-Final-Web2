from django import forms
from .models import Mii, Ilha

class MiiForm(forms.Form):
    class Meta:
        model=Mii
        fields='__all__'

    # def  __init__ ( self, *args, **kwargs ): 
    #     super (MiiForm, self).__init__(*args, **kwargs) 
    #     for visible in self.visible_fields(): 
    #         visible.field.widget.attrs[ 'class' ] = 'form-control'

class IlhaForm(forms.Form):
    class Meta:
        model=Ilha
        fields=('nome_ilha')

    # def  __init__ ( self, *args, **kwargs ): 
    #     super (IlhaForm, self).__init__(*args, **kwargs) 
    #     for visible in self.visible_fields(): 
    #         visible.field.widget.attrs[ 'class' ] = 'form-control'