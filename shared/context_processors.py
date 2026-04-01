from products.models import Product


def cart_context(request):
    cart_ids = request.session.get('cart', [])
    cart_products = Product.objects.filter(id__in=cart_ids, is_active=True)

    # Calculate total based on current language/currency
    total_uzs = sum(
        p.discount_price_uzs or p.price_uzs for p in cart_products
    )
    total_usd = sum(
        p.discount_price_usd or p.price_usd for p in cart_products
    )
    total_rub = sum(
        p.discount_price_rub or p.price_rub for p in cart_products
    )

    return {
        'cart_products': cart_products,
        'cart_count': len(cart_ids),
        'cart_total_uzs': total_uzs,
        'cart_total_usd': total_usd,
        'cart_total_rub': total_rub,
    }
