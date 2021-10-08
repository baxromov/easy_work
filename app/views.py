from django.http import HttpResponse
from django.views import generic

from app.forms import product


class HomeTemplateView(generic.TemplateView):
    template_name = 'app/main/index.html'


class ProductTemplateView(generic.TemplateView):
    template_name = 'app/main/product/index.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = product.ProductModelForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse(status=200)
        else:
            form = product.ProductModelForm(request.POST)
        return HttpResponse(status=400)

    def get_context_data(self, **kwargs):
        from app.models import product, category
        ctx = super(ProductTemplateView, self).get_context_data(**kwargs)
        category = category.Category.objects.all()
        ctx['products'] = product.Product.objects.all()
        return ctx
