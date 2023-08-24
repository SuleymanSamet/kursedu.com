from django.contrib import admin
from . models import Teacher


@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    search_fields = ('name',)
