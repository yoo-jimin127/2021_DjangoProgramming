from django.db import models

# Create your models here.
class blog(models.Model) :
    title = models.CharField(max_length=200) #제한이 있는 문자형 필드
    writer = models.CharField(max_length=100)
    pub_data = models.DateTimeField() #날짜와 시간을 저장해주는 필드
    body = models.TextField() #본문 : 제한이 없는 텍스트 필드 사용

    def __str__(self) :
        return self.title #메소드가 변경되었을 때 title 변경을 위한 self 호출

    def summary(self) :
        return self.body[:100]