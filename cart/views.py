from django.shortcuts import render
from django.shortcuts import render
from cart.models import Cart
from shop.models import Products
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def cart(request):
	print(request.user)
	if request.method=='POST':
		if request.POST.get('sub')=='Add To cart':	
			pid=request.POST.get('pid')
			product=Products.objects.get(pk=pid)
			qty=request.POST.get('qty')
			price=request.POST.get('amount')
			amount=float(qty)*float(price)
			print(product,qty,amount)
			item=Cart(user=request.user,product=product,product_qty=qty,product_amount=amount)
			item.save()
		if request.POST.get('sub')=='Delete':	
			
			item_id=request.POST.get('item_id')
			
			item=Cart.objects.get(pk=item_id)
			print(item_id,item)
			item.delete()
	cart=Cart.objects.filter(user=request.user)
	print(cart)	
	context={'cart':cart}
	return render(request,'cart/cart.html',context)