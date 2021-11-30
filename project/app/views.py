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
        for output in FactoryOwner.objects.all()]

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


class KeywordView(APIView):
    def post(self, request):
        serializer = KeywordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

class RecommendView(APIView):
    def get(self, request, user_id):
        keyword = KeywordList.objects.filter(user_id=user_id)
        serializer = KeywordSerializer(keyword, many=True)
        for data in serializer.data:
            if data['job'] == 'F':  # Founder
                list = FactoryInformation.objects.filter(keyword=data['keyword'])
                result = ListFactoryInfoSerializer(list, many=True)
                return Response(result.data, status=200)
            elif data['job'] == 'FO':  # Factory Owner
                list = FounderEstimate.objects.filter(keyword=data['keyword'])
                result = ListFoundeEstSerializer(list, many=True)
                return Response(result.data, status=200)
            else:
                return Response(status=500)
        return Response(status=200)












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

`http status code`
200 ~ success
300 ~ redirect
400 ~ client error
500 ~ server error

`주요 사용 코드`
200: 정상작동
201: 작성됨. 서버가 요청을 접수하고, 새 리소스를 작성했다.

301: 영구 이동, 요청한 페이지가 새 위치로 영구적으로 이동했다.
302: 임시 이동, 페이지가 현재 다른 위치에서 요청에 응답하고 있지만, 
     요청자는 향후 원래 위치를 계속 사용해야 한다.

400: 잘못된 요청
401: 권한없음
403 (Forbidden) : 필요한 권한을 가지고 있지 않아서, 요청을 거부
404: 서버에서 요청한 리소스를 찾을 수 없다.
405: 허용되지 않는 방법. POST 방식만을 지원하는 뷰에 GET 요청을 할 경우
"""
