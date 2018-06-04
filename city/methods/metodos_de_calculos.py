# -*- coding: utf-8 -*-
import statistics

import matplotlib.pyplot as plt

from city.models import City

cities = City.objects.all()
scores = [city.score for city in cities]


def calcular_valor_maximo():
    max_value = max(scores)
    return max_value


def calcular_valor_minimo():
    min_value = min(scores)
    return min_value


def calcular_amplitude_total():
    amplitude_total = max(scores) - min(scores)
    return amplitude_total


def calcular_media():
    media = statistics.mean(scores)
    return media


def calcular_mediana():
    mediana = statistics.median(scores)
    return mediana
    # f = 0  # frequencia acumulada da classe anterior a mediana
    # fm = 1  # frequencia simples absoluta da classe mediana - qtd de itens nela
    # h = 1  # Amplitude do intervalo da classe mediana ex.: 50 |- 54 => 4
    # md = lista.min("""limite inferior""") + (((lista.count() / 2) - f) / fm) * h


def calcular_moda():
    moda = statistics.mode(scores)
    return moda


def calcular_variancia():
    variancia = statistics.pvariance(scores)
    return variancia
    # n = 1  # tamanho da população
    # xi = 1  # conjunto de dados - ponto médio de cada classe
    # xm = 1  # media aritmetica da população
    # fi = 0  # frequencia absoluta de cada classe qtd * ponto_medio
    # total_simples = fi * xi
    # total_absoluto = fi * xi ** 2
    # variancia_populacional = ((xi - xm) ** 2) / n
    # variancia_amostral = total_absoluto - (total_simples ** 2) / len(lista) - 1


def calcular_desvio_padrao():
    desvio_padrao = statistics.pstdev(scores)
    return desvio_padrao
    # xi = 1  # conjunto de dados - ponto médio de cada classe
    # xm = 1  # media aritmetica da população
    # media = xi - xm
    # desvio_padrao_populacional = math.sqrt(media ** 2 / len(lista) - 1)
    # desvio_padrao_amostral = math.sqrt(media ** 2 / len(lista) - 1)


def calcular_coeficiente_de_variacao():
    desvio_padrao = calcular_desvio_padrao()
    media = calcular_media()
    coeficiente_de_variacao = desvio_padrao / media
    return coeficiente_de_variacao
    # coeficiente_de_variacao = desvio padrao / media
    # pegar os dados agrupados e os desagrupados

#
# def notas_medias(lista):
#     todas_notas_e = len(lista)  # somar todas as notas
#     xe = todas_notas_e / len(lista)
#     xi = 1  # conjunto de dados - ponto médio de cada classe
#     xm = 1  # media aritmetica das notas
#     variancia = todas_notas_e / todas_notas_e - (xe ** 2)  # ao quadrado e somando
#     desvio_padrao = math.sqrt(variancia)
#     calcular_desempenhos_individuais = (xi - xm) / desvio_padrao
#
#     calculo_nota_concurso = (((xi - xm) / desvio_padrao) * 100) + 500
