from django.contrib.messages.api import success
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm,CustomerForm,ProductForm
from django.forms import formsets, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm 
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth.models import Group

def dashboard(request):
  
    orders=Order.objects.all()
    products=Product.objects.all()
    context={'ord':orders,}
    return render(request,'accounts/dashboard.html',context)



def customers_list(request):
    customers=Customer.objects.all()
    total_customer=customers.count()
    context={'customers':customers,'total_customers':total_customer,}
    return render(request,'accounts/customers_list.html',context)


def stats(request):
    products=Product.objects.all()
    total_products=products.count()
    customers=Customer.objects.all()
    total_customer=customers.count()
    orders=Order.objects.all()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'total_products':total_products,'total_customers':total_customer,'total_orders':total_orders,'delivered':delivered,'pending':pending,}
    return render(request,'accounts/stats.html',context)




def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    total_orders=orders.count()
    context={'orders':orders,'customer':customer,'myFilter':myFilter,'total_orders':total_orders}
    return render(request,'accounts/customer.html',context)


def product(request):
    products=Product.objects.all()
    return render(request,'accounts/product.html',{'product':products})


def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=5)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none() ,instance=customer)
    #form=Orderform(initial={'customer':customer})
    
    if request.method=='POST':
        formset=OrderFormSet(request.POST,instance=customer)
  
        if formset.is_valid():
          
           formset.save()
           messages.success(request, "Successfully placed order")
           return redirect('/')
         
    context={'formset':formset,}
    return render(request,'accounts/order_form.html',context)


def updateOrder(request,pk):

    
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
  
        if form.is_valid():
          
           form.save()
           messages.success(request, "Successfully updated order")
           return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)


def deleteOrder(request,pk):

    
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'accounts/delete.html',context)



def Customer_form(request,id=0):
     
     
     
     if request.method=='GET':
         if id==0:
            form=CustomerForm()
         else:
             customer=Customer.objects.get(pk=id)
             form=CustomerForm(instance=customer)
             
         return render(request,'accounts/customer_form.html',{'form':form}) 
     else:

         if id==0:
             form=CustomerForm(request.POST)
         else:
             customer=Customer.objects.get(pk=id)
             form=CustomerForm(request.POST,instance=customer)
         if form.is_valid():
              form.save()
              messages.success(request, "Successfully created customer")
         return redirect('/')


def Update_form(request,pk):

             
    update=Order.objects.get(id=pk)
    form=OrderForm(instance=update) 
    if request.method=='POST':
        form=OrderForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated order")
            return redirect('/')   
    
    return render(request,'accounts/update_form.html',{'form':form})




def Product_form(request):
              
    
    form=ProductForm() 
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added product")
           
               
    
    return render(request,'accounts/update_form.html',{'form':form})





def bill(request,pk):
    orders=Order.objects.get(id=pk)
    context={'orders':orders}
    return render(request,'accounts/bill.html',context)


    

   


  
     


# Create your views here.
