#Agregando librerias framework#
from rest_framework import routers, serializers, viewsets

from Profile.models import Profile
from Profile.models import City
from Profile.models import Gender
from Profile.models import State
from Profile.models import MaritalStatus
from Profile.models import Occupation

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')

class GenderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('__all__')

class OccupationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ('__all__')

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('__all__')

class MaritalStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ('__all__')

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')