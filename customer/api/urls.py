from django.urls import path
from customer.api import views

urlpatterns = [
    path('list/', views.CustomerListAV.as_view(), name='customer_list'),
    path('<str:slug>/', views.CustomerDetailAV.as_view(), name='customer_detail'),
]