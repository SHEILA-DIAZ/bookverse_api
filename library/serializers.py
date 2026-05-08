from rest_framework import serializers
from .models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)
    autor_nacionalidad = serializers.CharField(source='autor.nacionalidad', read_only=True)

    class Meta:
        model = Libro
        fields = [
            'id',
            'titulo',
            'anio_publicacion',
            'genero',
            'autor',
            'autor_nombre',
            'autor_nacionalidad'
        ]
        