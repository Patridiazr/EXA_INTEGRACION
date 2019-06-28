from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'solicitud', views.SolicitudViewSet)

urlpatterns = [
   #NAVEGACION PAGINA
   path('',views.index,name="index"),
   path('',views.navbar,name="navbar"),
   path('',views.footer,name="footer"),
   path('productos/',views.productos,name="productos"),
   path('solicitud/',views.solicitud,name="solicitud"),
   path('administrador/',views.administrador,name="administrador"),
   path('regproducto/',views.regproducto,name="regproducto"),
   


   #CRUD USUARIOS
   path('crear_U',views.crear_U, name="crear_U"),


   #CRUD PRODUCTO LOGIN




   #CRUD PRODUCTOS GENERALES
   path('regproducto/crear_P',views.crear_P, name="crear_P"),
   path('administrador/eliminar_p/<int:id_prod>',views.eliminar_p, name="eliminar_p" ),
   path('administrador/editar_p/<int:id_prod>',views.editar_p, name="editar_p" ),






   #CRUD SOLICITUD
   path('crear_S',views.crear_S, name="crear_S"),
   path('administrador/eliminar_s/<int:id_solicitud>', views.eliminar_s, name="eliminar_s" ),
   path('administrador/editar_s/<int:id_solicitud>', views.editar_s, name="editar_s" ),
   


   #API'S
   path('api/', include(router.urls)), 
]