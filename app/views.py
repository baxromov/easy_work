from django.views import generic


class HomeTemplateView(generic.TemplateView):
    template_name = 'app/main/index.html'


class ProductTemplateView(generic.TemplateView):
    template_name = 'app/main/product/index.html'
