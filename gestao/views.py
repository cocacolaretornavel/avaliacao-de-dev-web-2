from django.shortcuts import render
from django.http import HttpResponse

eventos = {"Seminário de estatística": "Laboratório 01", "Semana de TI":"Auditório"}

def index(request):
    return HttpResponse("djfdjflk")

def dashboard(request):
    return render(request, "gestao/home.html", {"eventos:": eventos})

def novoregis(request):
    return HttpResponse("novo registro")
# Create your views here.
