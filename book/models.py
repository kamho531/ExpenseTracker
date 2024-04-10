from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category
    

class Book(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=500)
    publisher = models.CharField(max_length=150)
    published_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    distribution_expense = models.FloatField()

    def __str__(self):
        return self.title
