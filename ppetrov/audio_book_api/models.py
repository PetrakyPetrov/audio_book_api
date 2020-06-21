from django.db import models


class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    sample = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    chapter = models.ManyToManyField(Chapter)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
