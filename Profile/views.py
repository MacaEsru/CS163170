from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import Profile
from Profile.models import City
from Profile.models import State
from Profile.models import MaritalStatus
from Profile.models import Gender
from Profile.models import Occupation
# Importar Serializer
from Profile.serializer import ProfileSerializers
from Profile.serializer import CitySerializers
from Profile.serializer import StateSerializers
from Profile.serializer import MaritalStatusSerializers
from Profile.serializer import GenderSerializers
from Profile.serializer import OccupationSerializers


class ProfileList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = Profile.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = City.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = CitySerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = CitySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = State.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = StateSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = StateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaritalStatusList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = MaritalStatus.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = MaritalStatusSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = MaritalStatusSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenderList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = Gender.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = GenderSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = GenderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OccupationList(APIView):
    # Método GET para solciitar info
    def get(self, request, format=None):
        print("Método get")
        queryset = Occupation.objects.filter(delete = False)
        #many = True Si aplica si retorno  multiples objetos
        serializer = OccupationSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("Método post")
        serializer = OccupationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)