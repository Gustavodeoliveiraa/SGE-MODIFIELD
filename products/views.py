from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product
from categories.models import Category
from brands.models import Brand


class ProductLIstView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        queryset = super().get_queryset()
        if title:
            queryset = queryset.filter(title__icontains=title)
        if serie_number:
            queryset = queryset.filter(
                serie_number__icontains=serie_number
            )
        if brand:
            queryset = queryset.filter(brand_id=brand)
        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
