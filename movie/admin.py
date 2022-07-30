from django.contrib import admin
from .models import *

#모델을 등록했다면 어드민 페이지에 알려주는거 잊지 마세요!
admin.site.register(Movie)
admin.site.register(Staff)