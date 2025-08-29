from django.db import models

# Create your models here.
class Profile (models.Model):
    name = models.CharField(max_length=300),
    birthday = models.DateField(),
    height = models.FloatField(max_length=3),
    weight = models.FloatField(max_length=400)

class Question (models.Model):
    # Models Choices
    QUESTION_CATEGORY_CHOICES = {
        "AFO": "Atividades físicas ocupacionais",
        "EFL": "Exercícios físicos no lazer",
        "ALL": "Atividades físicas de lazer e locomoção",
    }
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=3, choices=QUESTION_CATEGORY_CHOICES)
    
class Choice (models.Model):
    name = models.CharField(max_length=300)
    question = models.models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.DecimalField(max_length=5)