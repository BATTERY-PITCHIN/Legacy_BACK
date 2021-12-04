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


class FounderEstSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderEstimate
        fields = '__all__'


class FactoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryInformation
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordList
        fields = ['user_id','keyword','job']