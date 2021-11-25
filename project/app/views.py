from django.shortcuts import render
from rest_framework.views import APIView
from . models import  *
from . serializer import *
from rest_framework.response import Response

# Create your views here.
class FounderView(APIView):
    def get(self, request):
        output = [
            {"id": output.id, 
            "name": output.name}
        for output in Founder.objects.all()]

        return Response(output, status=200)

    def post(self, request):
        serializer = FounderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def put(self, request): ...

    def delete(self, request): ...


class FactoryView(APIView):
    def get(self, request):
        output = [
            {"id": output.id, 
            "name": output.name}
        for output in Factory.objects.all()]

        return Response(output, status=200)

    def post(self, request):
        serializer = FactorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def put(self, request): ...

    def delete(self, request): ...