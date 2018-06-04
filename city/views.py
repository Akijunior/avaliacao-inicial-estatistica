# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from city.methods.metodos_de_calculos import *
from city.methods.metodos_histograma import *


def max_calculation_value(request):
    max_value = calcular_valor_maximo()
    return render(request, 'city/max_value.html',{'max_value': max_value})

def min_calculation_value(request):
    min_value = calcular_valor_minimo()
    return render(request, 'city/min_value.html',{'min_value': min_value})

def amplitude(request):
    amplitude = calcular_amplitude_total()
    return render(request, 'city/amplitude.html',{'amplitude': amplitude})

def show_media(request):
    media = calcular_media()
    return render(request, 'city/media.html',{'media': media})

def show_median(request):
    median = calcular_mediana()
    return render(request, 'city/median.html',{'median': median})

def show_mode(request):
    mode = calcular_moda()
    return render(request, 'city/mode.html',{'mode': mode})

def show_variance(request):
    variance = calcular_variancia()
    return render(request, 'city/variance.html',{'variance': variance})

def show_standard_deviation(request):
    standard_deviation = calcular_desvio_padrao()
    return render(request, 'city/standard_deviation.html',{'standard_deviation': standard_deviation})

def show_coefficient_of_variation(request):
    coefficient_of_variation = calcular_coeficiente_de_variacao()
    return render(request, 'city/coefficient_of_variation.html',{'coefficient_of_variation': coefficient_of_variation})

def show_histogram(request):
    histogram = gerador_de_histograma()
    return render(request, 'city/histogram.html',{'histogram': histogram})

def show_media_histogram(request):
    media = media_histograma()
    return render(request, 'city/histogram_media.html',{'media': media})

def show_median_histogram(request):
    median = mediana_histograma()
    return render(request, 'city/histogram_median.html',{'median': median})

def show_mode_histogram(request):
    mode = moda_histograma()
    return render(request, 'city/histogram_mode.html',{'mode': mode})

def show_variance_histogram(request):
    variance = variancia_populacional_histograma()
    return render(request, 'city/histogram_variance.html',{'variance': variance})

def show_standard_deviation_histogram(request):
    standard_deviation = desvio_padrao_populacional_histograma()
    return render(request, 'city/histogram_standard_deviation.html',
                  {'standard_deviation': standard_deviation})

def show_coefficient_of_variation_histogram(request):
    coefficient_of_variation = coeficiente_de_variacao_histograma()
    return render(request, 'city/histogram_coefficient_of_variation.html',
                  {'coefficient_of_variation': coefficient_of_variation})

# def iniciar():
#     # import csv
#     # import os
#     # path = "C:\\Users\\ljuni\\Desktop\\Python\\Django\\Estatistica\\primeira_avaliacao\\city"
#     # os.chdir(path)
#     # from city.models import City
#     # with open('paises_para_importacao.csv', encoding="utf8") as csvfile:
#     #     reader = csv.DictReader(csvfile)
#     #     for row in reader:
#     #         City.objects.create(name=row['no_cidade'], score=row['nota'], data_ref=row['data_ref'])
#     pass

def index(request):
    return render(request, 'city/page.html')

