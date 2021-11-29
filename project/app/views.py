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
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        NotImplementedError

    def delete(self, request):
        NotImplementedError


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
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        NotImplementedError

    def delete(self, request):
        NotImplementedError

"""
**STATUS CODE**
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED
"""
