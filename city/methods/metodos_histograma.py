# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import *
from city.models import City

cities = City.objects.all()
scores = [city.score for city in cities]
limite_corte_entre_classes = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]


# coeficiente de variação
def media_histograma():
    qtd_por_media = definir_valores_das_classes_histograma()
    valor_media = 0

    for i in range(len(limite_corte_entre_classes)):
        valor_media += qtd_por_media[i] * (limite_corte_entre_classes[i] - 0.5)
    valor_media /= len(cities)
    return valor_media


def mediana_histograma():
    qtd_por_media = definir_valores_das_classes_histograma()
    limite_medio = qtd_por_media[0]
    amp = 1
    cont = 0
    while limite_medio < len(scores) / 2:
        cont += 1
        limite_medio += qtd_por_media[cont]

    lim_inf = cont - 1
    fre_acu_ant_a_classe_med = limite_medio - qtd_por_media[cont]
    mediana = lim_inf + ((((len(scores)/ 2) - fre_acu_ant_a_classe_med)/ qtd_por_media[cont - 1])) * amp
    return mediana


def moda_histograma():
    ponto_medio_por_classe = []
    for i in range(len(limite_corte_entre_classes)):
        ponto_medio = (limite_corte_entre_classes[i] + 1) / 2
        ponto_medio_por_classe.append(ponto_medio)
    return ponto_medio_por_classe


def desvio_padrao_populacional_histograma():
    media = media_histograma()
    valor_media = 0
    qtd_por_media_ao_quadrado = definir_valores_das_classes_histograma()

    for i in range(len(limite_corte_entre_classes)):
        valor_media += (qtd_por_media_ao_quadrado[i] * limite_corte_entre_classes[i]) ** 2
    valor_media /= len(cities)
    desvio_padrao = sqrt(valor_media - (media ** 2))
    return desvio_padrao


def coeficiente_de_variacao_histograma():
    desvio_padrao = desvio_padrao_populacional_histograma()
    media = media_histograma()
    coeficiente_de_variacao = desvio_padrao/media

    return coeficiente_de_variacao


def variancia_populacional_histograma():
    qtd_por_media = definir_valores_das_classes_histograma()
    ponto_med_por_classe = moda_histograma()
    fre_simples = 0
    fre_composta = 0

    for i in range(len(qtd_por_media)):
        fre_simples += (qtd_por_media[i] * ponto_med_por_classe[i])
        fre_composta += (qtd_por_media[i] * (ponto_med_por_classe[i] ** 2))

    variancia_populacional = (fre_composta - ((fre_simples ** 2)/len(scores)))/len(scores)
    return variancia_populacional
    # media_populacional = media_histograma()
    #
    # for i in limite_corte_entre_classes:
    #     variancia_populacional += i - media_populacional
    # variancia_populacional /= len(scores)


# def variancia_amostral_histograma():
#     variancia_amostral = 0
#     media_populacional = media_histograma()
#
#     for i in limite_corte_entre_classes:
#         variancia_amostral += i - media_populacional
#     variancia_amostral /= len(scores)
#     return variancia_amostral


def gerador_de_histograma():
    y_axis = definir_valores_das_classes_histograma()
    x_axis = range(len(limite_corte_entre_classes))
    width_n = 0.8
    bar_color = 'green'

    bar = plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align="center", linewidth=10)
    plt.xticks(x_axis, gerador_de_nomes_para_labels(limite_corte_entre_classes))
    return plt
    # plt.show()
    # plt.save("histograma.png")


def gerador_de_nomes_para_labels(limite_corte_entre_classes):
    nomes = []
    for i in limite_corte_entre_classes:
        nomes.append("De %.2f \na %.2f\n" % (i - 1, i))
    return tuple(nomes)


def definir_valores_das_classes_histograma():
    # qtd_por_media = {}
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    seis = 0
    sete = 0
    oito = 0
    nove = 0
    dez = 0

    for i in scores:
        if i < 2:
            um += 1
        elif i < 3:
            dois += 1
        elif i < 4:
            tres += 1
        elif i < 5:
            quatro += 1
        elif i < 6:
            cinco += 1
        elif i < 7:
            seis += 1
        elif i < 8:
            sete += 1
        elif i < 9:
            oito += 1
        elif i < 10:
            nove += 1
        else:
            dez += 1
    # qtd_por_media["um"] = um
    #     # qtd_por_media["dois"] = dois
    #     # qtd_por_media["tres"] = tres
    #     # qtd_por_media["quatro"] = quatro
    #     # qtd_por_media["cinco"] = cinco
    #     # qtd_por_media["seis"] = seis
    #     # qtd_por_media["sete"] = sete
    #     # qtd_por_media["oito"] = oito
    #     # qtd_por_media["nove"] = nove
    #     # qtd_por_media["dez"] = dez
    qtd_por_media = []
    qtd_por_media.append(um)
    qtd_por_media.append(dois)
    qtd_por_media.append(tres)
    qtd_por_media.append(quatro)
    qtd_por_media.append(cinco)
    qtd_por_media.append(seis)
    qtd_por_media.append(sete)
    qtd_por_media.append(oito)
    qtd_por_media.append(nove)
    qtd_por_media.append(dez)

    return qtd_por_media
