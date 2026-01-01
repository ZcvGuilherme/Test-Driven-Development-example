def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def isPar(numero):
    return (numero % 2) == 0

def validarNumeroPositivo(numero):
    if numero == 0:
        raise ValueError
    return numero > 0