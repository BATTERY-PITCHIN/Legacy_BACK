# NOTE: 소프트웨어공학 드라이브에 있는 PITCH-IN:ERD Diagram을 기반으로 작성했습니다!! 21.11.30

from django.db import models

class User(models.Model):
    """
    `유저 통합 모델 클래스`

    유저 모델을 베이스로 창업주와 공장주 테이블을 상속
    :김태홍,2021.11.30

    add information
    :김태홍, 2021.12.05
    """
    id = models.CharField(
        help_text="User ID",
        max_length=20,
        blank=False,
        null=False,
        primary_key=True
    )
    password = models.CharField(
        help_text="User Password",
        max_length=20,
        blank=False,
        null=False
    )
    name = models.CharField(
        help_text="Founder Name",
        max_length=20,
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        help_text="phone number",
        max_length=12,
        blank=False,
        null=False
    )
    mail = models.CharField(
        help_text="E-Mail",
        max_length=20,
        blank=False,
        null=False
    )
    information = models.TextField(
        help_text="User Introduction"
    )
    # 사업자 번호(숫자), 계좌번호(숫자) 추가 요망


class Founder(User): 
    """
    `창업주 테이블`

    User 테이블을 상속받아 창업주로부터 필요한 데이터 저장
    :김태홍, 장성수, 21.11.30
    """
    corporate_name = models.CharField(
        help_text="corporate Name",
        max_length=20,
        blank=False,
        null=False
    )
    # 사업자 등록증(이미지), 법인 인감 증명서(이미지), 계좌번호(숫자) 추가 요망


class FactoryOwner(User):
    """
    `공장주 테이블`

    User 테이블을 상속받아 공장주로부터 필요한 데이터 저장
    :김태홍, 장성수, 21.11.30
    """
    company_name = models.CharField(
        help_text="company Name",
        max_length=20, 
        blank=False, 
        null=False
    )
    address = models.CharField(
        help_text="address",
        max_length=50, 
    )
    # 해당 카테고리는 공장의 범주로,
    # 견적서의 카테고리와는 다름!!
    category = models.CharField(
        help_text="category of factory sales", 
        max_length=10, 
        blank=True
    )
    # 공장 등록 번호(숫자) 추후 추가 요망


class FounderEstimate(models.Model):
    """
        `견적서 테이블`
        
            창업주가 작성한 견적서

        `견적서 데이터 베이스에 들어갈 내용`

            founder_id: 견적서를 작성한 사람(창업주)
            title: 견적서 이름
            item_name: 물건 이름 (ex. lipstick)
            category: 견적서 내용의 범주 (ex. Beauty)
            item_quantity: 물건 발주 필요 수량
            date: 작성일
            Keyword: 추천시 필요한 keyward
            content: 추가 설명

        :김태홍, 장성수, 21.11.30
    """
    founder_id = models.ForeignKey(
        "Founder",
        related_name="founder",
        on_delete=models.CASCADE,
        db_column="founder_id"
    )
    title = models.CharField(
        help_text="estimate title",
        max_length=200,
        blank=False,
        null=False 
    )
    item_name = models.CharField(
        help_text="item name",
        max_length=20, 
        blank=False,
        null=False
    )
    category = models.CharField(
        help_text="item category",
        max_length=20, 
        blank=False,
        null=False
    )
    item_quantity = models.IntegerField(
        help_text='item order quantity',
        blank=False,
        null=False
    )
    date = models.DateField(
        help_text="upload date",
        auto_now_add=True
    )
    keyword = models.CharField(
        help_text="keyword for recommandation",
        max_length=20
    )
    content = models.TextField(
        help_text="Informations of factory",
    )
    

class FactoryInformation(models.Model):
    """
        `공장 소개 테이블`

            창업주가 작성한 공장 소개 글 저장 클래스

        `공장 소개 데이터 베이스에 들어갈 내용`

            factoryowner_id: 공장 소개글을 작성한 사람(공장주)
            title: 견적서 이름
            content: 견적서 내용의 범주 (ex. Beauty)
            date: 작성일
            Keyword: 추천시 필요한 keyward

        :김태홍, 장성수, 21.11.30
    """
    factoryowner_id = models.ForeignKey(
        "FactoryOwner",
        related_name="factoryowner",
        on_delete=models.CASCADE,
        db_column="factoryowner_id"
    )
    title = models.CharField(
        help_text="estimate title",
        max_length=200,
        blank=False,
        null=False 
    )
    content = models.TextField(
        help_text="Informations of factory",
    )
    # thumbnail 이미지 추가 추후 개발 요망
    date = models.DateField(
        help_text="upload date",
        auto_now_add=True
    )
    keyword = models.CharField(
        help_text="keyword for recommandation",
        max_length=20
    )


class KeywordList(models.Model):
    """
    `키워드 테이블`

    유저들의 관심사를 키워드로 저장
    :김태홍, 장성수, 21.11.30
    """
    user_id = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        db_column="user_id"
    )
    keyword = models.CharField(
        help_text="keyword for recommandation",
        max_length=20,
        # null=False
    )
    job = models.CharField(
        help_text="FactoryOwner or Founder",
        max_length=10,
        null=False,
        blank=False
    )


class ContactUsers(models.Model):
    """
    `컨택 테이블`

    공장주와 창업주간 컨택이 된 사람들을 관리하기위한 테이블
    :김태홍, 장성수, 21.11.30
    """
    founder = models.ForeignKey(
        "Founder",
        related_name="founder_id",
        on_delete=models.CASCADE,
        db_column="founder"
    )
    factoryOwner = models.ForeignKey(
        "FactoryOwner",
        related_name="factory_owner_id",
        on_delete=models.CASCADE,
        db_column="factoryOwner"
    )
    start_date = models.DateField(
        help_text="start date",
        blank=False,
        null=False
    )
    end_date  = models.DateField(
        help_text="end date"
    )