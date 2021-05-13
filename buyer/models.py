from django.db import models
from EcommerceApp.models import Profile
from seller.models import Products

# Create your models here.
class Cart(models.Model):
	class Meta:
		unique_together = ('user' , 'product')
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Address(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	mobile = models.CharField(max_length=12)
	pincode = models.IntegerField()
	locality = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)
	landmark = models.CharField(max_length=40)