from django.db import models

# Create your models here.

class Mii(models.Model):
    nome_mii = models.CharField(
        max_length=20
    )
    idade_mii = models.IntegerField(
        default="?"
    )
    datadenascimento_mii = models.DateField(

    )
    comidasfavoritas_mii1 = models.TextField(

    )
    comidasfavoritas_mii2 = models.TextField(
        
    )
    personalidade_mii = models.TextField(
        # choices=[
        #     "Achiever (Busy Bee)", "Maverick (Individualist)", "Rogue (Individualist)", "Visionary (Leader)", "Buddy (Carer)", "Cheerleader (Optimist)", "Daydreamer (Dreamer)", "Sweetie (Softie)", "Charmer", "Dynamo (Hot-Blooded)", "Go-Getter (Adventurer)", "Merrymaker (Bubbly)", "Observer (Introvert)", "Perfectionist", "Thinker", "Strategist (Patient)"
        # ]
    )
    generomii = models.TextField(
        # choices=[
        #     "Masculine", "Feminine", 'Non-binary'
        # ]
    )
    generoquegostamii = models.TextField(
        # choices=[
        #     "Hetero", "Homo", "Bi"
        # ],
        # blank=True
    )