from django.shortcuts import render, HttpResponseRedirect
from . import models
from .models import Post
from django.http import HttpResponseNotFound

 
# получение данных из бд
def index(request):
    people = Post.objects.all()
    return render(request, "index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Post()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = Post.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Post.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
# Create your views here.
