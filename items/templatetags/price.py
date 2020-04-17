from django import template
from items.models import Order


register = template.Library()

@register.filter
def sub_total(quantity,price):
    return quantity * price

@register.filter
def total_price():
    total=0
    for orderitem in Order.items.all():
        total += orderitem.quantity*orderitem.item.total_price
    return total
