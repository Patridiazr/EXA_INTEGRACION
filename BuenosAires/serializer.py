
from rest_framework import serializers
from .models import Usuario, Solicitud

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url','username','email','password','direccion','ciudad','comuna')

class SolicitudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('url','nombres','email','asunto','mensaje','estado') 