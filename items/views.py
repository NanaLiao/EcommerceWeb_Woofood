from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(ListView):
    model = Item
    template_name='items/home.html'
    paginate_by = 8 #This limits the number of objects per page


class VegetablesView(ListView):
    model = Item
    template_name='items/category.html'
    paginate_by = 8
    queryset = Item.objects.filter(category='V')

class FruitView(ListView):
    model = Item
    template_name='items/category.html'
    paginate_by = 8
    queryset = Item.objects.filter(category='F')

class MeatView(ListView):
    model = Item
    template_name='items/category.html'
    paginate_by = 8
    queryset = Item.objects.filter(category='M')



class GroceryView(ListView):
    model = Item
    template_name='items/category.html'
    paginate_by = 8
    queryset = Item.objects.filter(category='G')


class MilkView(ListView):
    model = Item
    template_name='items/category.html'
    paginate_by = 8
    queryset = Item.objects.filter(category='MK')




class ItemDetailView(DetailView):

    model = Item
    template_name='items/product.html'


def order_summary(request):
    order=Order.objects.filter(user=request.user,ordered=False)[0]

    context = {'order':order}
    return render(request,'items/order_summary.html',context)



def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")

        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect ('items:order_summary')

def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect ('items:order_summary')
        else:
            messages.info(request, "You do not have an active order")
            return redirect ('items:order_summary')

def reduce_orderitem_quantity(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "The quantity of this item was reduced .")
            else:
                order.items.remove(order_item)
                order_item.delete()
                messages.info(request, "This item was removed")
            return redirect ('items:order_summary')
        else:
            messages.info(request, "You do not have this item")
            return redirect ('items:order_summary')

def add_orderitem_quantity(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The quantity of this item was added .")
            return redirect ('items:order_summary')
        else:
            messages.info(request, "You do not have this item")
            return redirect ('items:order_summary')

def check_out(request):
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
    context = {'order':order}

    return render(request,'items/checkout.html',context)
