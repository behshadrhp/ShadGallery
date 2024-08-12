from django.urls import path

from product import views


urlpatterns = [
    path('art/', views.ProductView.as_view(), name="products"),
]
