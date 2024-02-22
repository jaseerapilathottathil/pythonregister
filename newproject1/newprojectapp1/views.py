from django.http import HttpResponse
from django.shortcuts import render
from .models import student, teacher


# Create your views here.
def demo(request):
    obj= student.objects.all()
    obj1= teacher.objects.all()
    return render(request, 'index.html',{"result":obj,"teach":obj1})
