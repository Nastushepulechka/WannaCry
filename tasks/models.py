from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    status = models.ForeignKey('Status', null=True, on_delete=models.PROTECT)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Category(models.Model):
    category = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.category


class Tags(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags

