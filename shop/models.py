from django.db import models
import PIL


class Category(models.Model):
	category_name=models.CharField(max_length=257)
	def __str__(self):
		return str(self.category_name)

class Products(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	product_name=models.CharField(max_length=257)
	product_descreption=models.CharField(max_length=257)
	product_price=models.FloatField()
	product_image=models.ImageField(upload_to='products/') 
	def __str__(self):
		return self.product_name