from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('painelmii/ilha/<ilha_id>', views.painel_mii, name='painelmii'),
    path('painelilha/', views.painel_ilha, name='painelilha'),
    path('add_mii/ilha/<ilha_id>', views.add_mii, name='add_mii'),
    path('add_ilha', views.add_ilha, name='add_ilha'),
    path('edit_mii/ilha/<ilha_id>/mii/<id>', views.edit_mii, name='edit_mii'),
    path('edit_ilha/<id>', views.edit_ilha, name='edit_ilha'),
    path('del_mii/ilha/<ilha_id>/mii/<id>', views.del_mii, name='del_mii'),
    path('del_ilha/<id>', views.del_ilha, name='del_ilha'),
]
