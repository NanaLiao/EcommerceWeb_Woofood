from django import template
from items.models import Order


register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            count = 0
            for orderitem in qs[0].items.all():
                count +=orderitem.quantity
            return count

    return 0
