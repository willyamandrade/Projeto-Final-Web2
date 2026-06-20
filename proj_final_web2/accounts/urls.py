from django.urls import path
from . import views
urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('ativar/<uidb64>/<token>/', views.ativar_conta, name='ativa'),
]
