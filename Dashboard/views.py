from django.shortcuts import render

def cart(request):
	context = {}
	return render(request, 'Dashboard/cart.html', context)