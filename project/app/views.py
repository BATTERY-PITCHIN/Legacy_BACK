from django.shortcuts import render
from rest_framework.views import APIView
from . models import  *
from . serializer import *
from rest_framework.response import Response

# TODO: 모든 뷰 get 함수 수정하기 -> 어떤게 보여지는지에 따라 달라질듯


# Create your views here.
class FounderView(APIView):
    def get(self, request):
        founder = Founder.objects.all()
        serializer = FounderSerializer(founder, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = FounderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FactoryView(APIView):
    def get(self, request):
        factory = FactoryOwner.objects.all()
        serializer = FactorySerializer(factory, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = FactorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class KeywordView(APIView):
    def get(self, request):
        keyword = KeywordList.objects.all()
        serializer = KeywordSerializer(keyword, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = KeywordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

class RecommendView(APIView):
    def get(self, request, user_id):
        """
        `추천 리스트 받는 뷰`
        """
        # 사용자가 설정한 keyword로 부터 keyword 받아옴
        keyword = KeywordList.objects.filter(user_id=user_id)
        serializer = KeywordSerializer(keyword, many=True)
        # print(serializer.data)

        for data in serializer.data: # 사용자 데이터중 직업에 따라 보여지는 뷰 다르게 생성
            if data['job'] == 'founder':     # Founder 일때
                # 키워드를 통해 Factory 키워드 중 하나 선정 해서 
                recommend_list = FactoryInformation.objects.filter(keyword=data['keyword'])
                result = FactoryInfoSerializer(recommend_list, many=True)
                return Response(result.data, status=200)
            elif data['job'] == 'factory':  # Factory Owner 일때
                print(data['keyword'])
                recommend_list = FounderEstimate.objects.filter(keyword=data['keyword'])
                result = FounderEstSerializer(recommend_list, many=True)
                return Response(result.data, status=200)
            else:
                print("cannot recommand")
                return Response(status=500)
        # return Response(None, status=200)


class FounderEstView(APIView):
    def get(self, request):
        estimate = FounderEstimate.objects.all()
        serializer = FounderEstSerializer(estimate, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = FounderEstSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class FactoryInfoView(APIView): 
    def get(self, request):
        infomation = FactoryInformation.objects.all()
        serializer = FactoryInfoSerializer(infomation, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = FactoryInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



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
