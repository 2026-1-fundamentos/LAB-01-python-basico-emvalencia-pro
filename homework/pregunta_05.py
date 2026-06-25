"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    r = []
    with open('./files/input/data.csv') as f:
            for linea in f:
                lista = linea.split('\t')
                letra = lista[0]
                valor = int(lista[1])
                c=0
                for l in r:
                    if letra == l[0]:
                        max = l[1]
                        min = l[2]
                        if valor > max:
                            max = valor
                            l[1] = max
                        if valor < min:
                            min = valor
                            l[2] = min
                        c=1
                        break
                if c==0:
                    r.append([letra,int(lista[1]),int(lista[1])])
    r = list(map(tuple,r))
    r.sort()
    return(r)