from django.urls import path
from product.api.views import product_list, product_detail, Brand_list, \
    Brand_detail, Tag_detail, Tag_list

urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('<int:pk>/', product_detail, name="product_detail"),
    path('brand/', Brand_list.as_view(), name="brand-list"),
    path('brand/<int:pk>/', Brand_detail.as_view(), name="brand_detail"),

]

