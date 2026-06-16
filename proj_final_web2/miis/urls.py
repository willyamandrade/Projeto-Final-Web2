from django.urls import path
from . import views

urlpatterns = [
    path('painelmii', views.painel_mii, name='painel_mii'),
    path('painelilha', views.painel_ilha, name='painel_ilha'),
]
