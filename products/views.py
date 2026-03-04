from django.shortcuts import render


def products_list_view(request):
    return render(request, 'products/products-list.html')


def products_detail_view(request, pk):
    return render(request, 'products/product-detail.html')
