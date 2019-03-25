from django.db import models

class Category (models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    createBy   = models.CharField(max_length=50)
    createDate = models.DateTimeField('date created')
    updateBy   = models.CharField(max_length=50)
    updaeDate = models.DateTimeField('date updated')

class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    name    = models.DateTimeField('date published')
    image = models.ImageField()



    