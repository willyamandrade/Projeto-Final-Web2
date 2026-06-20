from django.db import models
from django.contrib.auth.models import User
from accounts.models import Perfil

# Create your models here.

class Ilha(models.Model):
    # Escolhas


    # Atributos/Campos
    nome_ilha = models.CharField()
    data_criacao_ilha = models.DateField(auto_now_add=True)
    proprietario_ilha = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    # Funções

    def __str__(self):
        return self.nome_ilha

class Mii(models.Model):
    # Escolhas
    personalidade_escolha = {"Achiever":"Achiever", "Maverick":"Maverick", "Rogue":"Rogue", "Visionary":"Visionary", "Buddy":"Buddy", "Cheerleader":"Cheerleader", "Cheerleader":"Daydreamer", "Sweetie":"Sweetie", "Charmer":"Charmer", "Dynamo":"Dynamo", "Go-Getter":"Go-Getter", "Merrymaker":"Merrymaker", "Observer":"Observer", "Perfectionist":"Perfectionist", "Thinker":"Thinker", "Strategist":"Strategist"}
    genero_escolha = {"Masculino":"Masculino", "Feminino":"Feminino", "Não-binário":'Não-binário'}
    generoquegosta_escolha = {"Hetero":"Hetero", "Homo":"Homo", "Bi":"Bi"}

    # Atributos/Campos

    nome_mii = models.CharField(
        max_length=20
    )
    idade_mii = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    datadenascimento_mii = models.DateField(
        blank=True,
        null=True,
    )
    comidafavorita1_mii = models.CharField(
        blank=True, null=True
    )
    comidafavorita2_mii = models.CharField(
        blank=True, null=True
    )
    personalidade_mii = models.CharField(
        choices=personalidade_escolha
    )
    genero_mii = models.CharField(
        choices=genero_escolha
    )
    generoquegosta_mii = models.CharField(
        choices=generoquegosta_escolha,
        blank=True,
        null=True
    )
    felicidade_mii = models.IntegerField(
        default=0
    )
    ilha_mii = models.ForeignKey(Ilha, on_delete=models.CASCADE)

    # Funções

    def __str__(self):
        return self.nome_mii