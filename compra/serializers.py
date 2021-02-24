from rest_framework import serializers
from .models import Articulo, File


class ListArtSerializer(serializers.ModelSerializer):
    class Meta():
        model = Articulo
        fields = "__all__"

class CompraSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    amount = serializers.IntegerField()
    
class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'timestamp')