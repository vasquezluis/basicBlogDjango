from distutils import text_file
from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request, 'main.html')


def password(request):

    text_gen = 'Hello'

    return render(request, 'pass_gen.html', {'password': text_gen})