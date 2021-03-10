import math

entrada = int(input('INgresa el año>>'))
entrada = entrada - 1

def dia_n():

    q = 31
    m = 12
    Y = entrada
    #math.floor Redondea numeors a enteros
    h = (q + math.floor((13 * (m + 1)) / 5) + Y + math.floor(Y / 4) - math.floor(Y / 100) + math.floor(Y / 400)) % 7

    return h + 1

dia_n()