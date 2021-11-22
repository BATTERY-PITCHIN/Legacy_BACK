from django.db import models

# Create your models here.
class React(models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=200)


class Founder(models.Model): ...


class Factory(models.Model): ...

    
class Estimate(models.Model):
    """
    견적서 테이블
    작성자: 김태홍
    날짜: 2021.11.22
    """
    id = models.BigAutoField(help_text="Estimate ID", primary_key=True)
    title = models.CharField(help_text="Estimate title", max_length=200, blank=False, null=False)
    contents = models.TextField(help_text="Estimate contents", blank=False, null=False)

class FactoryInfo(models.Model): ...


class Connected(models.Model): ...