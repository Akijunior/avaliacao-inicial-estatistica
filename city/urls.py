from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('max_value/', max_calculation_value, name='max_value'),
    path('min_value/', min_calculation_value, name='min_value'),
    path('amplitude/', amplitude, name='amplitude'),
    path('show_mode/', show_mode, name='show_mode'),
    path('show_media/', show_media, name='show_media'),
    path('show_median/', show_median, name='show_median'),
    path('show_variance/', show_variance, name='show_variance'),
    path('show_standard_deviation/', show_standard_deviation, name='show_standard_deviation'),
    path('show_coefficient_of_variation/', show_coefficient_of_variation, name='show_coefficient_of_variation'),

    path('frequence_table/', show_frequence_table, name='show_frequence_table'),
    path('frequence_distr_table/', show_freq_distr_table, name='show_freq_distr_table'),

    path('histogram/', show_histogram, name='show_histogram'),
    path('show_histogram_mode/', show_mode_histogram, name='show_mode_histogram'),
    path('show_histogram_media/', show_media_histogram, name='show_media_histogram'),
    path('show_histogram_median/', show_median_histogram, name='show_median_histogram'),
    path('show_histogram_variance/', show_variance_histogram, name='show_variance_histogram'),
    path('show_histogram_standard_deviation/', show_standard_deviation_histogram,
         name='show_standard_deviation_histogram'),
    path('show_histogram_coefficient_of_variation/', show_coefficient_of_variation_histogram,
         name='show_coefficient_of_variation_histogram'),
]