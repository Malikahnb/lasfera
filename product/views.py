from django.views.generic import ListView, TemplateView, DetailView

from product.models import ProductModel, ProductDetailModel


class ProductListView(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.order_by('-pk')


class ProductDetailView(DetailView):
    template_name = 'product-detail.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_detail'] = ProductDetailModel.objects.all()
        return context

