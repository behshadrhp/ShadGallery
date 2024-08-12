from django.shortcuts import render
from django.db.models import Q
from django.views import View

from product.models import Product


class ProductView(View):
    """
    This class is for rendering Product page.
    --> return all product.
    """

    def get(self, request):
        query = request.GET.get('q', '')
        products = Product.objects.select_related("user").all()

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__name__icontains=query)
            ).distinct()

        context = {
            'products': products,
            'query': query,
        }

        if request.htmx:
            return render(request, "gallery/product_list.html", context)
        return render(request, "gallery/products.html", context)
