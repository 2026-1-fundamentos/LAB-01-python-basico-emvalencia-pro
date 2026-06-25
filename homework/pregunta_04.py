"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    r = []
    with open('./files/input/data.csv') as f:
            for linea in f:
                lista = linea.split('\t')
                fecha = lista[2]
                mes = (fecha.split('-'))[1]
                c=0
                for l in r:
                    if mes == l[0]:
                        l[1] += 1
                        c=1
                        break
                if c==0:
                    r.append([mes,1])
    r = list(map(tuple,r))
    r.sort()
    return(r)
