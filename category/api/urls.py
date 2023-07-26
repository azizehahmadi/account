from django.urls import path
from category.api.views import CategoryListAV, CategoryDetailAV


urlpatterns = [
    path('list/', CategoryListAV.as_view(), name='category_list'),
    path('detail/<int:pk>/', CategoryDetailAV.as_view(), name='category-detail'),
]