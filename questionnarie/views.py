from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm
from .models import Question
# Create your views here.

def showForm(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('result', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'forms.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def result(request, pk):
    question = get_object_or_404(Question, pk=pk)
    total = question.total()
    return render(request, "result.html", {'total': total})
