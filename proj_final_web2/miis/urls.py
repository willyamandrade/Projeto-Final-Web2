from django.urls import path
from . import views

urlpatterns = [
    path('painelmii', views.painel_mii, name='painel_mii'),
    path('painelilha', views.painel_ilha, name='painel_ilha'),
    path('add_mii', views.add_mii, name='add_mii'),
    path('add_ilha', views.add_ilha, name='add_ilha'),

]
