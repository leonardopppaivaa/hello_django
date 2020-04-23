from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome, idade))

def soma(requests, valor1, valor2):
    soma_valores = valor1 + valor2
    return HttpResponse('<h1>A soma é {}.</h1>'.format(soma_valores))

def amor(requests, nome1, nome2):
    return HttpResponse('<h1>{} ama {}!</h1>'.format(nome1, nome2))

def subtracao(requests, valor1, valor2):
    sub_valores = valor1 - valor2
    return HttpResponse('<h1>A subtração é {}.</h1>'.format(sub_valores))

def multiplicacao(requests, valor1, valor2):
    mult_valores = valor1 * valor2
    return HttpResponse('<h1>A multiplicação é {}.</h1>'.format(mult_valores))

def divisao(requests, valor1, valor2):
    div_valores = valor1 / valor2
    return HttpResponse('<h1>A divisão é: {}.</h1>'.format(div_valores))