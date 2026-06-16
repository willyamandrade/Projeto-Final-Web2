from django.db import models
from django.contrib.auth.models import User
from accounts.models import Perfil
# Create your models here.

def criar_escolhas(escolhas : list):
        # Cria um dicionário genérico de escolhas que pode ser utilizado em campos de escolha CharField
        escolhas_legais = {}
        qtd_escolhas = len(escolhas)

        for i in range(qtd_escolhas):
            escolhas_legais[str(i)] = escolhas[i]

        return escolhas_legais

class Ilha(models.Model):
    # Escolhas


    # Atributos/Campos
    nome_ilha = models.CharField(

    )
    proprietario_ilha = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    # Funções

    def __str__(self):
        return self.nome_ilha

class Comida(models.Model):
    # Escolhas


    # Atributos/Campos
    sabor_comida = models.CharField(

    )
    nome_comida = models.CharField(

    )

    # Funções
    def __str__(self):
        return self.nome_comida

class Mii(models.Model):
    # Escolhas
    personalidade_escolha = {"0":"Achiever", "1":"Maverick", "2":"Rogue", "3":"Visionary", "4":"Buddy", "5":"Cheerleader", "6":"Daydreamer", "7":"Sweetie", "8":"Charmer", "9":"Dynamo", "10":"Go-Getter", "11":"Merrymaker", "12":"Observer", "13":"Perfectionist", "14":"Thinker", "15":"Strategist"}
    genero_escolha = {"0":"Masculine", "1":"Feminine", "2":'Non-binary'}
    generoquegosta_escolha = {"0":"Hetero", "1":"Homo", "2":"Bi"}

    # Atributos/Campos

    nome_mii = models.CharField(
        max_length=20
    ),
    idade_mii = models.PositiveIntegerField(
        blank=True
    ),
    datadenascimento_mii = models.DateField(
        blank=True
    ),
    comidasfavorita1_mii = models.OneToOneField(Comida, on_delete=models.SET_NULL,
        blank=True
    ),
    comidasfavorita2_mii = models.OneToOneField(Comida, on_delete=models.SET_NULL,
        blank=True
    ),
    personalidade_mii = models.CharField(
        choices=personalidade_escolha
    ),
    genero_mii = models.CharField(
        choices=genero_escolha
    ),
    generoquegosta_mii = models.CharField(
        choices=generoquegosta_escolha,
        blank=True
    ),
    felicidade_mii = models.IntegerField(

    ),
    ilha_mii = models.ForeignKey(Ilha, on_delete=models.SET_NULL),

    # Funções

    def __str__(self):
        return self.nome_mii