from django.shortcuts import render

# Create your views here.
def food_item( request ):
    template = 'Dashboard/food_list.html'
    return render(request,template)