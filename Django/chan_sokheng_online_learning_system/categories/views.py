from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/category_form.html', {'form': form})

def category_update(request, pk):
    category = Category.objects.filter(pk=pk).first()
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/category_form.html', {'form': form})

def category_delete(request, pk):
    category = Category.objects.filter(pk=pk).first()
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_delete.html', {'category': category})
