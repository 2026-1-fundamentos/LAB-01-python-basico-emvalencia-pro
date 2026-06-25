"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    r = []
    with open('./files/input/data.csv') as f:
            for linea in f:
                lista = linea.split('\t')
                dic = {}
                for s in lista[4].split(','):
                        clave, valor = s.split(':')
                        dic[clave] = int(valor)
                               
                for c,v in dic.items():
                    cont=0
                    for l in r:
                        if c == l[0]:
                            min = l[1]
                            max = l[2]
                            if v < min:
                                l[1] = v
                            if v > max:
                                l[2] = v
                            cont = 1
                    if cont == 0:
                        r.append([c,v,v])
    r = list(map(tuple,r))
    r.sort()
    return(r)
