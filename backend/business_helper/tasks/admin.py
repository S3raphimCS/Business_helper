from django.contrib import admin
from .models import Task, WorkObject, City


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkObject)
class ObjectAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
