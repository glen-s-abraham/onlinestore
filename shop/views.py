from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Products,Category
# Create your views here.
def landing(request,cat_id=1):
	if request.method=='POST':
		print(request.POST)
	categories=Category.objects.all()
	try:
		current=Category.objects.get(pk=cat_id)
	except:
		products=None
	else:
		products=Products.objects.filter(category=current)
		category=current.category_name
	context={'categories':categories,'products':products,'category':category}
	return render(request,'shop/landing.html',context)

def descrpetion(request,pid):
	product=Products.objects.get(pk=pid)
	context={'product':product}
	return render(request,'shop/descreption.html',context)
