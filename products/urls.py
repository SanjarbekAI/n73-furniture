from django.urls import path

from products.views import products_list_view, products_detail_view

app_name = 'products'

urlpatterns = [
    path('', products_list_view, name='list'),
    path('<int:pk>/', products_detail_view, name='detail'),
]
