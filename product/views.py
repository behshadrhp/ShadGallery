from django.shortcuts import render
from django.views import View
from django.db.models import Q

from .models import Product

class ProductView(View):
    def get(self, request):
        """
        get products -> apply filtering.
        """
        query = request.GET.get("q", "")
        products = Product.objects.select_related("user").all()

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__name__icontains=query)
            ).distinct()

        context = {"products": products, "query": query}

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render(request, "gallery/product_list.html", context)

        return render(request, "gallery/products.html", context)
