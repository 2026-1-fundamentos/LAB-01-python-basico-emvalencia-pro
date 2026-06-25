"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    r = []
    with open('./files/input/data.csv') as f:
            r.append([next(f)[0],1])
            for linea in f:
                lista = linea.split('\t')
                letra = lista[0]
                c=0
                for l in r:
                    if letra == l[0]:
                        l[1] += int(lista[1])
                        c=1
                        break
                if c==0:
                    r.append([letra,int(lista[1])])
    r = list(map(tuple,r))
    r.sort()
    return(r)
                