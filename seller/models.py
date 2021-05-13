from django.db import models
from EcommerceApp.models import Profile

# Create your models here.

class Category(models.Model):
	catname = models.CharField(max_length=30)

class Products(models.Model):
	pname = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	qty = models.IntegerField()
	desc = models.CharField(max_length=100)
	pic = models.ImageField(upload_to='proimage',blank=True,)
	added_by = models.ForeignKey(Profile, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	dated = models.DateTimeField(auto_now_add = True)

class Photo(models.Model):
	pics = models.ImageField(upload_to='newimage', blank=True)