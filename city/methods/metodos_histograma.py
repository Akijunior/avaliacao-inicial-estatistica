# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import *
from city.models import City

cities = City.objects.all()
scores = [city.score for city in cities]
total = len(scores)
limite_corte_entre_classes = [3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9.0, 9.5, 10]

def corte_de_notas():
    corte = []
    for i in limite_corte_entre_classes:
        a = "%.1f |- %.1f" % (i, i + 0.5)
        corte.append(a)
    return corte


def gerar_tabela_de_frequencia():
    notas = corte_de_notas()
    fi = definir_valores_das_classes_histograma()
    xi = moda_histograma()
    fi_xi_list = []
    fi_xi_quad_list = []

    for i in range(len(xi)):
        fi_xi = fi[i] * xi[i]
        fi_xi_quad = fi[i] * pow(xi[i], 2)
        fi_xi_list.append(fi_xi)
        fi_xi_quad_list.append(fi_xi_quad)

    tabela_de_frequencias = {}
    tabela_de_frequencias['notas'] = notas
    tabela_de_frequencias['fi'] = fi
    tabela_de_frequencias['xi'] = xi
    tabela_de_frequencias['fi_xi_list'] = fi_xi_list
    tabela_de_frequencias['fi_xi_quad_list'] = fi_xi_quad_list

    return tabela_de_frequencias


def createLinesForHTML(dicio):
    indice = len(dicio['fi'])
    matriz = []
    vetor = []
    for i in range(0,indice):
        for key in dicio:
            vetor.append(dicio[key][i])
        matriz.append(vetor)
        vetor = []
    return matriz


def criar_tabela_de_distr_de_frequencia():
    classes = corte_de_notas()
    fi = definir_valores_das_classes_histograma()
    xi = moda_histograma()
    fri = []
    fi_acu = []
    fri_acu = []
    freq_acu = 0
    freq_acu_rel = 0

    for i in range(len(xi)):
        freq_simp_rel = fi[i]/total
        freq_acu += fi[i]
        freq_acu_rel += freq_simp_rel
        fri.append(freq_simp_rel)
        fi_acu.append(freq_acu)
        fri_acu.append(freq_acu_rel)

    tabela_de_frequencias = {}
    tabela_de_frequencias['classes'] = classes
    tabela_de_frequencias['fi'] = fi
    tabela_de_frequencias['xi'] = xi
    tabela_de_frequencias['fri'] = fri
    tabela_de_frequencias['fi_acu'] = fi_acu
    tabela_de_frequencias['fri_acu'] = fri_acu

    return tabela_de_frequencias


def media_histograma():
    qtd_por_media = definir_valores_das_classes_histograma()
    valor_media = 0

    for i in range(len(limite_corte_entre_classes)):
        valor_media += qtd_por_media[i] * (limite_corte_entre_classes[i] - 0.5)
    valor_media /= total
    return valor_media


def mediana_histograma():
    qtd_por_media = definir_valores_das_classes_histograma()
    limite_medio = qtd_por_media[0]
    amp = 1
    cont = 0
    while limite_medio < total / 2:
        cont += 1
        limite_medio += qtd_por_media[cont]

    lim_inf = cont - 1
    fre_acu_ant_a_classe_med = limite_medio - qtd_por_media[cont]
    mediana = lim_inf + ((((len(scores)/ 2) - fre_acu_ant_a_classe_med)/ qtd_por_media[cont - 1])) * amp
    return mediana


def moda_histograma():
    ponto_medio_por_classe = []
    for i in range(len(limite_corte_entre_classes)):
        ponto_medio = (limite_corte_entre_classes[i] + (limite_corte_entre_classes[i] - 1)) / 2
        ponto_medio_por_classe.append(ponto_medio)
    return ponto_medio_por_classe


def desvio_padrao_populacional_histograma():
    media = media_histograma()
    valor_media = 0
    qtd_por_media_ao_quadrado = definir_valores_das_classes_histograma()

    for i in range(len(limite_corte_entre_classes)):
        valor_media += (qtd_por_media_ao_quadrado[i] * limite_corte_entre_classes[i]) ** 2
    valor_media /= total
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

    variancia_populacional = (fre_composta - ((fre_simples ** 2)/total))/total
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
        nomes.append("De %.2f \na %.2f\n" % (i - 0.5, i))
    return tuple(nomes)


def definir_valores_das_classes_histograma():
    tres_meio = 0
    quatro = 0
    quatro_meio = 0
    cinco = 0
    cinco_meio = 0
    seis = 0
    seis_meio = 0
    sete = 0
    sete_meio = 0
    oito = 0
    oito_meio = 0
    nove = 0
    nove_meio = 0
    dez = 0

    for i in scores:
        if i < 3.5:
            tres_meio += 1
        elif i < 4:
            quatro += 1
        elif i < 4.5:
            quatro_meio += 1
        elif i < 5:
            cinco += 1
        elif i < 5.5:
            cinco_meio += 1
        elif i < 6:
            seis += 1
        elif i < 6.5:
            seis_meio += 1
        elif i < 7:
            sete += 1
        elif i < 7.5:
            sete_meio += 1
        elif i < 8:
            oito += 1
        elif i < 8.5:
            oito_meio += 1
        elif i < 9:
            nove += 1
        elif i < 9.5:
            nove_meio += 1
        else:
            dez += 1

    qtd_por_media = []
    qtd_por_media.append(tres_meio)
    qtd_por_media.append(quatro)
    qtd_por_media.append(quatro_meio)
    qtd_por_media.append(cinco)
    qtd_por_media.append(cinco_meio)
    qtd_por_media.append(seis)
    qtd_por_media.append(seis_meio)
    qtd_por_media.append(sete)
    qtd_por_media.append(sete_meio)
    qtd_por_media.append(oito)
    qtd_por_media.append(oito_meio)
    qtd_por_media.append(nove)
    qtd_por_media.append(nove_meio)
    qtd_por_media.append(dez)

    return qtd_por_media
