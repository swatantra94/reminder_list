from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from reminderlist import models,forms
from django.views.generic.edit import DeleteView

# Create your views here.
def index(request):
    todolist = models.Todolist.objects.all()
    context = {
        "todolist":todolist
    }
    return render(request,'reminderlist/index.html',context)

def activity(request,pk):
    activity = get_object_or_404(models.Todolist,pk=pk)
    context = {
        "activity":activity
    }
    return render(request, 'reminderlist/activity.html',context)

def create(request):
    form = forms.TodolistForms()
    context={
        "form":form
    }
    if request.method=="POST":
        form = forms.TodolistForms(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/reminderlist/todo/')
    return render(request,'reminderlist/create.html',context)

def delete(request,pk):
    models.Todolist.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/reminderlist/todo/')