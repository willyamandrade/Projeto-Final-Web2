from django.db import models

# Create your models here.

class Mii(models.Model):
    # Escolhas
    personalidade_escolha = {
        "1":"Achiever (Busy Bee)",
        "2":"Maverick (Headstrong)",
        "3":"Rogue (Individualist)",
        "4":"Visionary (Leader)",
        "5":"Buddy (Carer)",
        "6":"Cheerleader (Optimist)",
        "7":"Daydreamer (Dreamer)",
        "8":"Sweetie (Softie)",
        "9":"Charmer",
        "10":"Dynamo (Hot-Blooded)",
        "11":"Go-Getter (Adventurer)",
        "12":"Merrymaker (Bubbly)",
        "13":"Observer (Introvert)",
        "14":"Perfectionist",
        "15":"Thinker",
        "16":"Strategist (Patient)"
    }
    genero_escolha = {"1":"Masculine", "2":"Feminine", "3":'Non-binary'}
    generoquegosta_escolha = {"1":"Hetero", "2":"Homo", "3":"Bi"}

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

    # Funções