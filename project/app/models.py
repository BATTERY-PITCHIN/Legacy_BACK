from django.db import models

# Create your models here.
# basic code
# class React(models.Model):
#     employee = models.CharField(max_length=30)
#     department = models.CharField(max_length=200)


class Founder(models.Model): 
    """
    창업주 테이블
    작성자: 김태홍, 김연수
    날짜: 2021.11.25
    """
    founder_id = models.BigAutoField(help_text="Founder ID", primary_key=True)
    founder_name = models.CharField(help_text="Founder name", max_length=20, blank=False, null=False)
    


class Factory(models.Model):
    """
    공장 테이블
    작성자: 김태홍, 김연수
    날짜: 2021.11.25
    """
    factory_id = models.BigAutoField(help_text="Factory ID", primary_key=True)
    factory_name = models.CharField(help_text="Factory name", max_length=20, blank=False, null=False)


class Estimate(models.Model):
    """
    견적서 테이블: 창업주가 작성한 견적서
    작성자: 김태홍
    날짜: 2021.11.25
    """
    estimate_id = models.BigAutoField(help_text="Estimate ID", primary_key=True)
    estimate_title = models.CharField(help_text="Estimate title", max_length=200, blank=False, null=False)
    estimate_contents = models.TextField(help_text="Estimate contents", blank=False, null=False)
    founder_id = models.ForeignKey("Founder", related_name="founder", on_delete=models.CASCADE, db_column="founder_id")

class FactoryInfo(models.Model):
    """
    공장 소개 테이블
    작성자: 김태홍, 김연수
    날짜: 2021.11.25
    """
    # id, 제품, 장소, 소개글, 산업 분야(키워드), 대표자 이름, 이메일, H.P,  
    factory_profile_id = models.BigAutoField(help_text="Estimate ID", primary_key=True)
    factory_profile_title = models.CharField(help_text="Estimate title", max_length=200, blank=False, null=False)
    factory_profile_contents = models.TextField(help_text="Estimate contents", blank=False, null=False)
    factory_id = models.ForeignKey("Factory", related_name="factory", on_delete=models.CASCADE, db_column="factory_id")


class Connected(models.Model): 
    """
    매칭된 테이블
    작성자: 김태홍, 김연수
    날짜: 2021.11.25
    """


# 추후 chat.models에 기록할 예정
class chatting(models.Model): ...