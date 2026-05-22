from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def criar_escolhas(escolhas : list):
        # Cria um dicionário genérico de escolhas que pode ser utilizado em campos de escolha CharField
        escolhas_legais = {}
        qtd_escolhas = len(escolhas)

        for i in range(qtd_escolhas):
            escolhas_legais[str(i)] = escolhas[i]

        return escolhas_legais

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfis/', null=True, blank=True)
    email_confirmado = models.BooleanField(default=False)

class Mii(models.Model):
    # Escolhas
    personalidade_escolha = {"0":"Achiever", "1":"Maverick", "2":"Rogue", "3":"Visionary", "4":"Buddy", "5":"Cheerleader", "6":"Daydreamer", "7":"Sweetie", "8":"Charmer", "9":"Dynamo", "10":"Go-Getter", "11":"Merrymaker", "12":"Observer", "13":"Perfectionist", "14":"Thinker", "15":"Strategist"}
    genero_escolha = {"0":"Masculine", "1":"Feminine", "2":'Non-binary'}
    generoquegosta_escolha = {"0":"Hetero", "1":"Homo", "2":"Bi"}

    # Atributos/Campos

    nome_mii = models.CharField(
        max_length=20
    )
    idade_mii = models.PositiveIntegerField(
        blank=True
    )
    datadenascimento_mii = models.DateField(
        blank=True
    )
    comidasfavoritas_mii1 = models.CharField(
        blank=True
    )
    comidasfavoritas_mii2 = models.CharField(
        blank=True
    )
    personalidade_mii = models.CharField(
        choices=personalidade_escolha
    )
    generomii = models.CharField(
        choices=genero_escolha
    )
    generoquegostamii = models.CharField(
        choices=generoquegosta_escolha,
        blank=True
    )
    felicidade_mii = models.IntegerField(

    )

    # Funções

    


class Ilha(models.Model):
    # Escolhas


    # Atributos/Campos
    nome_ilha = models.CharField(

    )
    proprietario_ilha = models.CharField(
        
    )
    # Funções

    

class Item(models.Model):
    # Escolhas


    # Atributos/Campos
    nome_item = models.CharField(

    )
    categoria_item = models.CharField(

    )

    # Funções

    

class Comida(Item):
    # Escolhas


    # Atributos/Campos
    sabor_comida = models.CharField(

    )

    # Funções

    

class Observacao(models.Model):
    # Escolhas


    # Atributos/Campos
    titulo_obs = models.CharField(

    )
    horario_obs = models.TimeField(

    )
    data_obs = models.DateField(

    )
    descricao_obs = models.CharField(

    )

    # Funções

    