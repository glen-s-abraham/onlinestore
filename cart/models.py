from django.db import models

from django.db import models
from shop.models import Products 
from django.contrib.auth.models import User



class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Products,on_delete=models.CASCADE)
	product_qty=models.IntegerField()
	product_amount=models.FloatField()
	def __str__(self):
		return str(self.product)

class Orders(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Products,on_delete=models.CASCADE)
	product_qty=models.IntegerField()
	product_amount=models.FloatField()
	def __str__(self):
		return str(self.product)
