from django.shortcuts import render, redirect
from .forms import ProfileForm, QuestionForm
# Create your views here.

def showForm(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = QuestionForm()
    return render(request, 'forms.html', {'form': form})

def success(request):
    return render(request, 'success.html')


