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

class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = '__all__'

class FactoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryInfo
        fields = '__all__'

# class ConnectedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Connected
#         fields = ['__all__']

