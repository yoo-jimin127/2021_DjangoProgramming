from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import blog

admin.site.register(blog) #만든 사이트를 admin에 등록하는 과정