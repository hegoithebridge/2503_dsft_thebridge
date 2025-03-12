import math

def ejercicio_1(dia):
    dias_semana = {1: "Lunes",
               2: "Martes",
               3: "Miércoles",
               4: "Jueves",
               5: "Viernes",
               6: "Sábado",
               7: "Domingo"}
    return dias_semana.get(dia, "Día erróneo")

def ejercicio_2(tamaño:int=5):
    lista_8 = list(range(int(tamaño),0,-1))
    while len(lista_8) > 0:
        print(*lista_8)
        lista_8.pop(0)

def ejercicio_3(num_1, num_2):
    if num_1 == num_2:
        out = "Son iguales"
    elif num_1 > num_2:
        out = "Primer número mayor que segundo"
    else:
        out = "Segundo número mayor que primero"
    return out

def limpieza_texto(texto, dict_vocales={'á':'a',
                                        'é':'e',
                                        'í':'i',
                                        'ó':'o',
                                        'ú':'u'}):
    texto = texto.lower()

    for clave in dict_vocales:
        texto = texto.replace(clave, dict_vocales[clave])
    return texto

def ejercicio_4(frase, letra):
    frase = limpieza_texto(frase)
    return frase.count(letra.lower())

def ejercicio_5(frase):

    dict_conteo = {}
    frase = limpieza_texto(frase)

    for caracter in frase:
        if caracter not in dict_conteo.keys() and caracter not in [" ", ","]:
            dict_conteo[caracter] = frase.count(caracter)

    return dict_conteo

def ejercicio_6(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento)
        except:
            print("El elemento no se encuentra en la lista")
    else:
        print("Comando no reconocido")
    return lista

def ejercicio_7(*args):
    return " ".join(args)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def cuadrado(l, n=1):
    return round(n * l ** 2, 2)

def triangulo(b, a):
    return round(b * a / 2, 2)

def circulo(r):
    return round(math.pi * r ** 2, 2)



if __name__ == "__main__":
    print(triangulo(3,7))
    print(circulo(10))
    print()
    