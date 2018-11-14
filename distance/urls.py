from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from distance import views

urlpatterns = [
    path('distance/', views.results_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)