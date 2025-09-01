from django.db import models

# Create your models here.
class Profile (models.Model):
    name = models.CharField(max_length=300),
    birthday = models.DateField(),
    height = models.FloatField(),
    weight = models.FloatField()

class Question (models.Model):
    # Models Choices
    QUESTION_VALUES = [
        (1, "Nunca"),
        (2, "Raramente"),
        (3, "Às vezes"),
        (4, "Frequentemente"),
        (5, "Sempre"),
    ]
    
    QUESTION_VALUES_REVERSE = [
        (1, "Muito frequentemente"),
        (2, "Frequentemente"),
        (3, "Às vezes"),
        (4, "Raramente"),
        (5, "Nunca"),
    ]
    
    QUESTION_VALUES_WEIGHT = [
        (5, "Muito mais pesado"),
        (4, "Mais pesado"),
        (3, "Iguamente pesado"),
        (2, "Mais leve"),
        (1, "Muito mais leve"),
    ]
    
    QUESTION_VALUES_EQUAL = [
        (5, "Muito maior"),
        (4, "Maior"),
        (3, "Igual"),
        (2, "Mais leve"),
        (1, "Muito mais leve"),
    ]
    question_2 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="No trabalho, eu fico sentado:")
    question_3 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="No trabalho, eu fico em pé")
    question_4 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="No trabalho, eu ando:")
    question_5 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="No trabalho, eu levanto objetos pesados:")
    question_6 = models.IntegerField(choices=QUESTION_VALUES_REVERSE, verbose_name="Depois do trabalho, eu me sinto cansado:")
    question_7 = models.IntegerField(choices=QUESTION_VALUES_REVERSE, verbose_name="No trabalho, eu suo:")
    question_8 = models.IntegerField(choices=QUESTION_VALUES_WEIGHT, verbose_name="Em comparação com o trabalho de outras pessoas da minha idade, o meu trabalho é fisicamente:")
# Falta questão 9 (Ela está em aberto)
    question_10 = models.IntegerField(choices=QUESTION_VALUES_EQUAL, verbose_name="Em comparação com outras pessoas da minha idade, minha atividade física durante os momentos de lazer é:")
    question_11 = models.IntegerField(choices=QUESTION_VALUES_REVERSE, verbose_name="Durante os momentos de lazer eu suo:")
    question_12 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="Durante os momentos de lazer, eu pratico atividades físicas:")
    question_13 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="Durante os momentos de lazer, eu assisto televisão:")
    question_14 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="Durante os momentos de lazer, eu ando:")
    question_15 = models.IntegerField(choices=QUESTION_VALUES, verbose_name="Durante os momentos de lazer, eu ando de bicicleta:")
# Falta questão 16 (Ela está em aberto)
 
# Cálculo questões categoria AFO    
    def AFO(self):
        totalAFO = (
            #Falta questão 1
            (self.question_2) +
            (self.question_3) +
            (self.question_4) +
            (self.question_5) +
            (self.question_6) +
            (self.question_7) +
            (self.question_8)
            / 8
        )
        
        # Montar cálculo        

        return totalAFO
        
# Cálculo questões categoria ELF
    def ELF(self):
        totalELF = (
            # Falta questão 9
            (self.question_10) +
            (self.question_11) +
            (self.question_12)
            / 4
        )
        
        # Montar cálculo
        
        return totalELF
        
# Cálculo questões categoria ALL
    def ALL(self):
        totalALL = (
            (6 - (self.question_13)) +
            (self.question_14) +
            (self.question_15)
            # Falta questão 14
            /4
        )

        # Montar cálculo
        
        return totalALL
    
    def total(self):
        return self.ALL() + self.ELF() + self.AFO()