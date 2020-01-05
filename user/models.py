from django.db import models

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetails(models.Model):
	#creates a relation with User model
	user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	mobile=models.CharField(max_length=12)
	address=models.TextField()
	def __str__(self):
		return self.user.username
