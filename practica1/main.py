import math 
import numpy as np
import random


def aleatorios():
    individuos = []
    
    for i in range(0,10):
        cadena = format((random.randint(0, 15)), 'b')
        individuos.append(cadena)

    return individuos


def evaluar(cadena):
    numero = int(str(cadena),2)
    return funcion(numero)

def funcion(x):
    numerador = x-5
    denominador = 2 + math.sin(x)
    return abs(numerador/denominador)

def valores_fx(individuos):
    f_x = []
    p_sel = []
    p_sel_acum = []
    for i in individuos: 
        f = evaluar(i)
        f_x.append(f)
       

    suma = sum(f_x)
    #print(suma)
    for i in f_x: 
        f = i/suma
        p_sel.append(f)

    acumulador = 0   
    for p in p_sel:
        acumulador+=p
        p_sel_acum.append(acumulador)


    return p_sel_acum

def seleccion_padres(p_sel_acum):
    padres = []
    valor1 = random.uniform(0, 1)
    padre1 = 0
    print(valor1)
    for p in p_sel_acum:
        if(p>=valor1):
            padre1 = p
            break
            

    
    padre2 = padre1
    while(padre2==padre1):
        valor2 = random.uniform(0, 1)
        for p in p_sel_acum:
            if(p>=valor2):
                padre2 = p
                break
    
    padres = [padre1,padre2]
    return padres


def ruleta():
    individuos = aleatorios()
    p_sel_acum = valores_fx(individuos)
    print(p_sel_acum)
    padres = seleccion_padres(p_sel_acum)
    print(padres)

if __name__ == "__main__":
    
    ruleta()

    #

    #print()
    #print(evaluar(individuos[0]))
