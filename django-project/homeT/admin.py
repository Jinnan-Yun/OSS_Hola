from django.contrib import admin

#[JY] User Model 작업때문에 잠시 주석처리합니다.-> 다시 살림
from .models import Video, Like, Tag

# Register your models here.
admin.site.register(Video)

from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import WorkOutCategory
from .models import AgeCategory


class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields']+=('age','nickname', 'workingout')
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('age','nickname','workingout')}),
    )

class TagAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(User, CustomUserAdmin)
admin.site.register(WorkOutCategory)
admin.site.register(AgeCategory)
admin.site.register(Tag)
