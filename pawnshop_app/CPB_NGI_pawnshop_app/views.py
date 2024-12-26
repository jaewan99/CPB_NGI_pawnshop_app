from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def mainsite(request):
   allCustomer = customer_test.objects.all()
   return render (request, 'index.html', {'allCustomer':allCustomer})


def addCustomer(request):
   if(request.method == "POST"):
      custName = request.POST.get("custName")
      customer_test.objects.create(customer_name=custName)
      

   return redirect('mainsite')

