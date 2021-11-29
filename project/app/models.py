from django.db import models

# Create your models here.
# basic code
# class React(models.Model):
#     employee = models.CharField(max_length=30)
#     department = models.CharField(max_length=200)


class Founder(models.Model): 
    """
    창업주 테이블
    작성자: 김태홍
    날짜: 2021.11.25
    """
    name = models.CharField(help_text="Founder Name", \
        max_length=20, blank=False, null=False)
    interest_keyword = models.CharField(help_text="Keyword1", \
        max_length=10, blank=True)
    # 추후 모델에 추가할 내용
    # 이메일, 전화번호 등 인적사항들


class Factory(models.Model):
    """
    공장 테이블
    작성자: 김태홍
    날짜: 2021.11.25
    """
    name = models.CharField(help_text="Factory Name", \
        max_length=20, blank=False, null=False)
    interest_keyword = models.CharField(help_text="Keyword1", \
        max_length=10, blank=True)
    # 대표자 이름, 이메일, H.P 등 인적사항, 홈페이지 등


class Founder_Est(models.Model):
    """
    견적서 테이블: 창업주가 작성한 견적서
    작성자: 김태홍
    날짜: 2021.11.25
    """
    founder_id = models.ForeignKey("Founder", related_name="founder_est", \
        on_delete=models.CASCADE, db_column="founder_id")
    title = models.CharField(help_text="Estimate Title", \
        max_length=200, blank=False, null=False)
    contents = models.TextField(help_text="Estimate Contents", \
        blank=False, null=False)
    keyword1 = models.CharField(help_text="Keyword1", \
        max_length=10, blank=True)
    keyword2 = models.CharField(help_text="Keyword2", \
        max_length=10, blank=True)
    keyword3 = models.CharField(help_text="Keyword3", \
        max_length=10, blank=True)
    

class Factory_Introd(models.Model):
    """
    공장 소개 테이블
    작성자: 김태홍
    날짜: 2021.11.25
    """
    # id, 제품, 장소, 소개글, 산업 분야(키워드),   
    factory_id = models.ForeignKey("Factory", related_name="factory_introd",\
        on_delete=models.CASCADE)#related_name이 Factory_introd로 해야하는거아님?
    title = models.CharField(help_text="Introduction Title", \
        max_length=200, blank=False, null=False)
    contents = models.TextField(help_text="Introduction Contents", \
        blank=False, null=False)
    keyword1 = models.CharField(help_text="Keyword1", \
        max_length=10, blank=True)
    keyword2 = models.CharField(help_text="Keyword2", \
        max_length=10, blank=True)
    keyword3 = models.CharField(help_text="Keyword3", \
        max_length=10, blank=True)



# class Connected(models.Model): 
#     """
#     매칭된 테이블
#     
#     """


# # 추후 chat.models에 기록할 예정
# class chatting(models.Model): ...