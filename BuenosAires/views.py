from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Usuarios.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Solicitud, ProduI, Producto

# Create your views here.
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')
def footer (request):
    return render (request,'footer.html')
def productos (request):
    productos = Producto.objects.all()
    contexto = {'productos':productos}
    return render (request,'productos.html',contexto)
def solicitud (request):
    return render (request,'solicitud.html')
def administrador (request):
    usuario = Usuario.objects.all()
    solicitud = Solicitud.objects.all()
    productos = Producto.objects.all()
    contexto = {'usuario':usuario,'solicitud':solicitud,'productos':productos}
    return render (request,'administrador.html',contexto)
def regproducto (request):
    return render (request,'regproducto.html')

#import de api
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .serializer import SolicitudSerializer


#CRUD USUARIOS
def crear_U(request):
    username = request.POST.get('username','')
    correo = request.POST.get('correo','')
    contra = request.POST.get('contra','')
    direccion = request.POST.get('direccion','')
    ciudad = request.POST.get('ciudad','')
    comuna = request.POST.get('comuna','')
    usuario = Usuario(username=username,correo=correo,contra=contra,direccion=direccion,ciudad=ciudad,
    comuna=comuna)
    usu = User.objects.create_user(email=correo,password=contra)
    usuario.save()
    usu.save()
    return redirect('index')

#Eliminar usuario
def eliminar_u(request,id_usu):
    usu = Usuario.objects.get(id=id_usu)
    usu.delete()
    return redirect('administrador')

#CRUD PRODUCTOS GENERALES
def crear_P(request):
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get ('descripcion')
    precio = request.POST.get('precio')
    prod = Producto(titulo=titulo,descripcion=descripcion,precio=precio)
    prod.save()
    return HttpResponse('<script>alert("Producto Ingresado ");'+
                        ' window.location.href="/";</script>')

#Editar PRODUCTO
def editar_p(request,id_prod):
    producto = Producto.objects.get(pk=id_prod)
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    producto.titulo = titulo
    producto.descripcion = descripcion
    producto.save()
    return HttpResponse('<script>alert("Producto Editado ");'+
                        ' window.location.href="/";</script>')

#Eliminar PRODUCTO
def eliminar_p(request,id_prod):
    s = Producto.objects.get(id=id_prod)
    s.delete()
    return HttpResponse('<script>alert("Producto Eliminado ");'+
                        ' window.location.href="/";</script>')



#CRUD SOLICITUDES
def crear_S(request):
    nombres = request.POST.get('nombres')
    direccion = request.POST.get('direccion')
    email = request.POST.get('email')
    asunto = request.POST.get('asunto')
    mensaje = request.POST.get('mensaje')
    estado = request.POST.get('estado')
    sol = Solicitud(nombres=nombres,direccion=direccion,email=email,asunto=asunto,mensaje=mensaje,estado=estado)
    sol.save()
    return HttpResponse('<script>alert("Solicitud ingresada correctamente");'+
                        ' window.location.href="/";</script>')

#Editar Servicio
def editar_s(request,id_solicitud):
    solicitud = Solicitud.objects.get(pk=id_solicitud)
    estado = request.POST.get('estado')
    solicitud.estado = estado
    solicitud.save()
    return redirect('administrador')

#Eliminar servicio
def eliminar_s(request,id_solicitud):
    s = Solicitud.objects.get(id=id_solicitud)
    s.delete()
    return redirect('administrador')

#Serialyzer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer