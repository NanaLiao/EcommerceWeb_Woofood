from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib import messages




CATEGORY_CHOICES = (
    ('F', 'Fruit'),
    ('V', 'Vegetables'),
    ('M', 'Meat'),
    ('MK','Milk'),
    ('G','Grocery'),
)


LABEL_CHOICES = (
    ('D', 'Discount'),
    ('O', 'Out of stock'),

)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1,default='')
    slug = models.SlugField(default='product')
    description=models.TextField()
    photo = models.ImageField(upload_to='food_photos', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('items:product_detail',kwargs={'slug':self.slug}) #if it is return redirect, it should be return redirect ('items:product_detail',slug=slug)

    def add_to_cart_url(self):
        return reverse('items:add_to_cart',kwargs={'slug':self.slug})

    def remove_from_cart_url(self):
        return reverse('items:remove_from_cart',kwargs={'slug':self.slug})

    def reduce_orderitem_quantity_url(self):
        return reverse('items:reduce_orderitem_quantity',kwargs={'slug':self.slug})

    def add_orderitem_quantity_url(self):
        return reverse('items:add_orderitem_quantity',kwargs={'slug':self.slug})





class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null='True')
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def sub_total(self):
        if self.item.discount_price:
            sub_total = self.quantity*self.item.discount_price
        else:
            sub_total = self.quantity*self.item.price
        return sub_total

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem,related_name='orders')
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total = 0
        for orderitem in self.items.all():
            total += orderitem.sub_total()
        return total

    def total_quantity(self):
        total = 0
        for orderitem in self.items.all():
            total += orderitem.quantity
        return total
