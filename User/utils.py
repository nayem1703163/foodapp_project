import json
from .models import *

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.User
		order, created = Order.objects.get_or_create(customer=user, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	return {'cartItems':cartItems ,'order':order, 'items':items}
