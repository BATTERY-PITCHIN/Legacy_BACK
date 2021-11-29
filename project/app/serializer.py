from rest_framework import serializers
from . models import *

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'

class Founde_EstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder_Est
        fields = '__all__'

class Factory_IntrodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory_Introd
        fields = '__all__'

# class ConnectedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Connected
#         fields = ['__all__']

