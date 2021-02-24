from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from rest_framework import status
from .models import Articulo
from .serializers import ListArtSerializer, CompraSerializer, FileSerializer


# Create your views here.


class ListArt(ListAPIView):
    serializer_class = ListArtSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Articulo.objects.all()

class RegisterCompra(APIView):
    serializer_class = CompraSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CompraSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data["name"]
        amount = serializer.validated_data["amount"]

        art = Articulo.objects.get(name=name)

        return Response({"compra correcta":200, "nombre del producto": art.name,
                        "cantidad": amount, "total": amount*art.price})


from unipath import Path
#import pandas as pd
from rest_framework.parsers import MultiPartParser, FormParser

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    #authentication_classes = (TokenAuthentication,)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():

            file_serializer.save()
            
            BASE_DIR = Path(__file__).ancestor(3)
            MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'api_carrito')
            print(MEDIA_ROOT + file_serializer.data["file"])
            #excel = pd.read_excel(MEDIA_ROOT + file_serializer.data["file"])
            #print(excel.head())
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)