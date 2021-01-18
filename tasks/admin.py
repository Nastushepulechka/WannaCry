from django.contrib import admin
from django.db import models
from tasks.models import Tasks, Category, Tags, Status
from import_export.admin import ImportExportModelAdmin

def change_ToDo(modeladmin, request, queryset):
    queryset.update(status='1')
    change_ToDo.short_description = "Изменить статус на ToDo"

def change_InProgress(modeladmin, request, queryset):
    queryset.update(status='2')
    change_InProgress.short_description = "Изменить статус на InProgress"

def change_Done(modeladmin, request, queryset):
    queryset.update(status='3')
    change_Done.short_description = "Изменить статус на Done"

@admin.register(Tasks)
class TasksAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'content', 'published', 'status')
    list_display_links = ('title', 'category')
    list_filter = ("category", "status")
    search_fields = ("title__startswith",)
    actions = [change_ToDo, change_InProgress, change_Done]
    pass


#admin.site.register(Tasks, TasksAdmin)
admin.site.register(Category)
admin.site.register(Status)

# STATUS_CHOICES = (
#     (1, 'ToDo'),
#     (2, 'InProgress'),
#     (3, 'Done'),
# )
#
# class Article(models.Tasks):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES)
#
#     def __str__(self):
#         return self.title
