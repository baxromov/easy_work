import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from app.forms import product, registration


class Registration(generic.CreateView):
    form_class = registration.RegistrationForm
    template_name = 'app/authentication/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super(Registration, self).form_valid(form)

    def form_invalid(self, form):
        return super(Registration, self).form_invalid(form)


class HomeTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/main/index.html'


class ProductTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/main/product/index.html'

    def post(self, request, *args, **kwargs):
        from app.models import product as user_products
        if request.method == 'POST':
            form = product.ProductModelForm(request.POST, files=request.FILES)
            if form.is_valid():
                user_products.Product.objects.create(user=request.user,
                                                     name=form.cleaned_data['name'],
                                                     category=form.cleaned_data['category'],
                                                     measurement=form.cleaned_data['measurement'],
                                                     price=form.cleaned_data['price'],
                                                     quantity=form.cleaned_data['quantity'],
                                                     image=form.cleaned_data['image'],
                                                     )
                return HttpResponse(status=200)
        else:
            form = product.ProductModelForm(request.POST)
        return HttpResponse(status=400)

    def get_context_data(self, **kwargs):
        from app.models import product, category
        ctx = super(ProductTemplateView, self).get_context_data(**kwargs)
        products = product.Product.objects.filter()

        ctx['categories'] = category.Category.objects.filter(user=self.request.user)
        return ctx


def product_json(request):
    from app.models import product
    from django.core import serializers
    products = product.Product.objects.filter(user=request.user)
    product_data = [{
        "name": item.name,
        "category": item.category.name,
        "measurement": item.measurement,
        "price": item.price,
        "quantity": item.quantity,

    } for item in products]
    json = serializers.serialize('json', products)
    return HttpResponse(json, content_type='application/json')
