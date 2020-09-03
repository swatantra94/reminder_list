from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from reminderlist import models,forms
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    todolist = models.Todolist.objects.all()
    context = {
        "todolists":todolist,
    }
    return render(request,'reminderlist/index.html',context)

@login_required(login_url='/auth/login')
def activity(request,pk):
    activity = get_object_or_404(models.Todolist,pk=pk)
    context = {
        "activity":activity
    }
    return render(request, 'reminderlist/activity.html',context)
    
@login_required(login_url='/auth/login')
def create(request):
    form = forms.TodolistForms()
    context={
        "form":form
    }
    if request.method=="POST":
        form = forms.TodolistForms(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/todo/')
    return render(request,'reminderlist/create.html',context)
    
@login_required(login_url='/auth/login')
def delete(request,pk):
    models.Todolist.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/todo/')

@login_required(login_url='/auth/login')
def wall(request):
    posts = models.Todolist.objects.all()
    a=[]
    for post in posts:
        if post.user.id==request.user.id:
            a.append(post)
    context={
        "a":a
    }
    return render(request,'reminderlist/wall.html',context)


def comment(request, pk):
    post = get_object_or_404(models.Todolist, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/todo/')
    else:
        form = forms.CommentForm()
    return render(request, 'reminderlist/comment.html', {'form': form})