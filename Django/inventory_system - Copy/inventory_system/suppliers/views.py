from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_add(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_add.html', {'form': form})

def supplier_update(request, pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_update.html', {'form': form})

def supplier_delete(request, pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_delete.html', {'supplier': supplier})