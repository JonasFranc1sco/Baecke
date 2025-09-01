from django import forms
from models import Profile, Question, Choice

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['name', 'birthday', 'height', 'weight']

class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = ['name', 'category']