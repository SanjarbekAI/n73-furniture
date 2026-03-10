from django.shortcuts import render

from products.models import Product, ProductCategory, ProductTag, ProductColor, Manufacture


def products_list_view(request):
    products = Product.objects.filter(is_active=True)

    manufacture = request.GET.get('manufacture')

    tag = request.GET.get('tag')
    color = request.GET.get('color')

    if manufacture:
        products = products.filter(manufacture__id=int(manufacture))

    context = {
        "products": products,
        "categories": ProductCategory.objects.filter(is_active=True),
        "tags": ProductTag.objects.all(),
        "colors": ProductColor.objects.all(),
        "manufactures": Manufacture.objects.filter(is_active=True),
    }
    return render(request,
                  'products/products-list.html',
                  context=context
                  )


def products_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk, is_active=True)
    except Product.DoesNotExist:
        return render(request, 'shared/404.html')

    context = {
        "product": product
    }
    return render(request,
                  'products/product-detail.html',
                  context=context
                  )
