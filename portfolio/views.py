from django.shortcuts import render
# obtener el modelo de la base de datos
from .models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects})