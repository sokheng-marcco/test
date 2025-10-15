from django.shortcuts import render
from customers.models import Customer
from products.models import Product
from sales.models import Order
from django.db.models import Sum
from employees.decorators import employee_login_required


def dashboard_home(request):
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
        
    order_amount = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'total_products': total_products,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'order_amount': order_amount,
    }
    return render(request, 'dashboard/home.html', context)