from django.contrib import admin
from django.urls import path
from EcoGarden import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inspiracoes/', views.inspiracoes, name='inspiracoes'),
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('calculadora/', views.calcular_valor, name='calcular_valor'),
    path('economia_agua/', views.economia_agua, name='economia_agua'),
    path('adicionar/', views.add_servico, name="add_servico"),
]
    
