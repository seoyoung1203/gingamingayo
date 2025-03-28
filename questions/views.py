from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
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

def detail(request, id):
    question = Question.objects.get(id=id)
    
    context = {
        'question': question,
    }

    return render(request, 'detail.html', context)

def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:detail', id=id)
    else:
        form = QuestionForm(instance=question)

    context = {
        'form': form
    }

    return render(request, 'update.html', context)

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('questions:index')

def comment_create(request, question_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            question = Question.objects.get(id=question_id)
            comment.qustion = question
            comment.save()
            return redirect('questions:detail', id)
    else:
        return redirect('questions:index')



