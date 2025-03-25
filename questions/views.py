from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }

    return render(request, 'index.html', context)

def create(request):
    
    if request.method == 'POST':
        form = QuestionForm(request.POST) 
        if form.is_valid:
            form.save()
            return redirect('questions:index')
       
    else:
        forms = QuestionForm()

    context = {
        'forms' : forms,
    }

    return render(request, 'create.html', context)
