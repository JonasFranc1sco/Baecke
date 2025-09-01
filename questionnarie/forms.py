from django import forms
from .models import Profile, Question

class CleanRadioSelectMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                # Remove a opção em branco e força sem default selecionado
                choices = field.choices
                field.choices = [(val, label) for val, label in choices if val is not None and val != '']
                field.initial = None
                
class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['name', 'birthday', 'height', 'weight']

class QuestionForm(CleanRadioSelectMixin, forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_2', 'question_3', 'question_4', 'question_5', 'question_6',
                  'question_7', 'question_8','question_10','question_11','question_12',
                  'question_13', 'question_14','question_15'] 
        widgets = {
            'question_2': forms.RadioSelect(),
            'question_3': forms.RadioSelect(),
            'question_4': forms.RadioSelect(),
            'question_5': forms.RadioSelect(),
            'question_6': forms.RadioSelect(),
            'question_7': forms.RadioSelect(),
            'question_8': forms.RadioSelect(),
            'question_10': forms.RadioSelect(),
            'question_11': forms.RadioSelect(),
            'question_12': forms.RadioSelect(),
            'question_13': forms.RadioSelect(),
            'question_14': forms.RadioSelect(),
            'question_15': forms.RadioSelect(),
        }
