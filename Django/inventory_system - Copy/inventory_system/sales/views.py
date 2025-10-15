from django.shortcuts import render,redirect
from .models import Order
from .forms import OrderForm,OrderDetailForm,OrderDetailFormSet

def order_list(request):
    orders = Order.objects.select_related('customer', 'employee').all()
    return render(request, 'sales/order_list.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            formset = OrderDetailFormSet(request.POST, instance=order)

            if formset.is_valid():
                order.save()
                order_details = formset.save(commit=False)
                for item in order_details:
                    item.total_price = item.product.selling_price * item.quantity
                    item.save()
                formset.save_m2m()
                order.save()
                return redirect('order_list')
        else:
            formset = OrderDetailFormSet(request.POST)
    else:
        form = OrderForm()
        formset = OrderDetailFormSet()
    return render(request, "sales/order_create.html", {'form': form, 'formset': formset})


def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'sales/order_detail.html', {'order': order})