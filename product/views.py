from django.shortcuts import render
from django.views import View

from product.models import Product


class ProductView(View):
    """
    This class is for rendering Product page.
    --> return all product.
    """

    def get(self, request):
        products = Product.objects.select_related("user").all()

        context = {"products": products}
        return render(request, "gallery/products.html", context)
