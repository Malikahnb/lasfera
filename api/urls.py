from django.urls import path

from api.views import ProductModelListAPIView

urlpatterns = [
    path('products/', ProductModelListAPIView.as_view())
]