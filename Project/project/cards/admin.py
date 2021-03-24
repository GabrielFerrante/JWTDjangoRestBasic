from django.contrib import admin

# Register your models here.
from .models import Card, Task

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','status', 'owner']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','description', 'done', 'card']