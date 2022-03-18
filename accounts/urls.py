from django.urls import path
from. import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('customers_list/',views.stats,name='stats'),
    path('stats/',views.customers_list,name='customers_list'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('product/',views.product,name='product'),
    path('order_form/<str:pk>',views.createOrder,name='create_order'),
    path('update_form/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),
    path('customer_form/<int:id>',views.Customer_form,name='customer_form'),
    path('customer_form/',views.Customer_form,name='customer_form'),
    path('update_form_dash/<str:pk>',views.Update_form,name='update_form_'),
    path('product_form/',views.Product_form,name='product_form'),
    path('bill/<str:pk>',views.bill,name='bill'),
]