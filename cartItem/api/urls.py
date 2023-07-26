from django.urls import path
from cartItem.api.views import cartItemListAV,cartItemDetailListAV, cartItemById, cartItemDetailById,\
    customer_cartDetail, customer_cartDetail_create, cat_cart_Item, cat_cart_Item_create

urlpatterns = [
    path('list/', cartItemListAV.as_view(), name='cart-list'),
    path('list/<int:pk>', cartItemById.as_view(), name='list-by-Id'),

    path('list-detail/', cartItemDetailListAV.as_view(), name='cart-de-list'),
    path('list-detail/<int:pk>', cartItemDetailById.as_view(), name='cart-de-byId'),


    path('customer/<int:pk>/cartdetail/', customer_cartDetail.as_view(), name='customer_cartDetail'),
    path('customer/<int:pk>/cartdetail-create/', customer_cartDetail_create.as_view(), name='customer_cartDetail_create'),

    path('category/<int:pk>/cartdetail/', cat_cart_Item.as_view(), name='cat-cartDetail'),
    path('category/<int:pk>/cartdetail-create/', cat_cart_Item_create.as_view(), name='cat-cartDetail-create'),



    
]