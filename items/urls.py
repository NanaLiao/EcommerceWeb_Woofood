from django.urls import path
from . import views
from .views import  *


app_name ="items"
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('vegetables/',VegetablesView.as_view(), name='vegetable'),
    path('meat/',MeatView.as_view(), name='meat'),
    path('milk/',MilkView.as_view(), name='milk'),
    path('fruit/',FruitView.as_view(), name='fruit'),
    path('grocery/',GroceryView.as_view(), name='grocery'),

    path('product/<slug:slug>/',ItemDetailView.as_view(), name='product_detail'),
    path('order/',views.order_summary, name='order_summary'),
    path('add_to_cart/<slug:slug>/',views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>/',views.remove_from_cart, name='remove_from_cart'),
    path('reduce_orderitem_quantity/<slug:slug>/',views.reduce_orderitem_quantity, name='reduce_orderitem_quantity'),
    path('add_orderitem_quantity/<slug:slug>/',views.add_orderitem_quantity, name='add_orderitem_quantity'),
    path('check_out/',views.check_out, name='check_out'),



]
