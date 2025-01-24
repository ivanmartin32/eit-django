from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from datetime import datetime
from core import models
# Create your views here.

def saludar(request):
	return HttpResponse('Hola Django')

def saludar_hola(request):
	return HttpResponse('<h1> Hola a todos desde ivis </h1>')

def saludar_con_parametros(request, nombre:str, apellido:str):
	nombre = nombre.capitalize()
	apellido = apellido.upper()
	return HttpResponse(f'{nombre}, {apellido}')

def index(request):
	lista = []
	while len(lista) <= 10:
		aleatorio = randint(1,10)
		lista.append(aleatorio)
	ano_actual = datetime.now().year
	context = {'año': ano_actual,
			'numero': aleatorio,
			'lista': lista}
	return render(request, 'core/index.html', context)

def client_list(request):
	clientes = models.Cliente.objects.all()
	return render(request,'core/client_list.html', {'clientes': clientes})