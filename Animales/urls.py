from django.urls import path
from.import views

urlpatterns = [
        path('animal',views.animal_list, name='Animal_list'),
        path('protectora',views.protectora_list, name='Protectora_list'),
        path('colaborador',views.colaborador_list, name='Colaborador_list'),
]
