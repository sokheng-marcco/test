from django.shortcuts import render, HttpResponse, redirect
from .models import Customer
from .forms import CustomerAddForm, CustomerEditForm

# CUSTOMER VIEWS
def customer_list(request):
    customers = Customer.objects.all()
    return render(request,"customers/customer_list.html",{"customers":customers})

def customer_add(request):
    form = CustomerAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("customer_list")
    return render(request,"customers/customer_add.html",{"form":form})

def customer_edit(request,pk):
    customer = Customer.objects.filter(pk=pk).first()
    form = CustomerEditForm(request.POST or None,instance = customer)
    if form.is_valid():
        form.save()
        return redirect("customer_list")
    return render(request,"customers/customer_edit.html",{"form":form})

def customer_delete(request,pk):
    customer = Customer.objects.filter(pk=pk).first()
    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")
    return render(request,"customers/customer_delete.html",{"customer":customer})

