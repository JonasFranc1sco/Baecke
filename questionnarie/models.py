from django.db import models

# Create your models here.
class Profile (models.Model):
    name = models.CharField(max_length=300),
    birthday = models.DateField(),
    height = models.FloatField(max_length=3),
    weight = models.FloatField(max_length=400)

class Question (models.Model):
    # Models Choices
    QUESTION_CATEGORY = {
        "AFO": "Atividades físicas ocupacionais",
        "EFL": "Exercícios físicos no lazer",
        "ALL": "Atividades físicas de lazer e locomoção",
    }
    
    QUESTION_VALUES = {
        (1, "Nunca"),
        (2, "Raramente"),
        (3, "Às vezes"),
        (4, "Frequentemente"),
        (5, "Sempre"),
    }
    
    QUESTION_VALUES_REVERSE = {
        (1, "Muito frequentemente"),
        (2, "Frequentemente"),
        (3, "Às vezes"),
        (4, "Raramente"),
        (5, "Nunca"),
    }
    
    QUESTION_VALUES_WEIGHT = {
        (5, "Muito mais pesado"),
        (4, "Mais pesado"),
        (3, "Iguamente pesado"),
        (2, "Mais leve"),
        (1, "Muito mais leve"),
    }
    
    QUESTION_VALUES_EQUAL = {
        (5, "Muito maior"),
        (4, "Maior"),
        (3, "Igual"),
        (2, "Mais leve"),
        (1, "Muito mais leve"),
    }
    
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=3, choices=QUESTION_CATEGORY)
    
    question_2 = models.IntegerField(choices=QUESTION_VALUES)