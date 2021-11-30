from rest_framework import serializers
from . models import *

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryOwner
        fields = '__all__'

class FoundeEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderEstimate
        fields = '__all__'

class FactoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryInformation
        fields = '__all__'

class ListFoundeEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderEstimate
        fields = ['founder_id', 'title', 'category', 'keyword']

class ListFactoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryInformation
        fields = ['factoryowner_id', 'title', 'keyword']

# class ConnectedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Connected
#         fields = ['__all__']

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordList
        fields = ['user_id','keyword','job']