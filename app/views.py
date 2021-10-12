from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app.forms import product, registration, category


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

    def get_context_data(self, **kwargs):
        from app.models import product
        ctx = super(ProductTemplateView, self).get_context_data(**kwargs)
        ctx['products'] = product.Product.objects.filter(user=self.request.user)
        return ctx


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'app/main/product/create.html'
    form_class = product.ProductModelForm
    success_url = reverse_lazy('product')

    def get_form(self, form_class=None):
        f = super().get_form(form_class)
        f.fields['category'].queryset = self.request.user.category_set.all()
        return f

    def form_valid(self, form):
        self.product = form.save(commit=False)
        user = self.request.user
        self.product.user = user
        self.product.user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    from app.models.product import Product
    template_name = 'app/main/product/update.html'
    form_class = product.ProductModelForm
    model = Product
    success_url = reverse_lazy('product')

    def get_form(self, form_class=None):
        f = super().get_form(form_class)
        f.fields['category'].queryset = self.request.user.category_set.all()
        return f

    def form_valid(self, form):
        self.product = form.save(commit=False)
        user = self.request.user
        self.product.user = user
        self.product.user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    from app.models import category
    template_name = 'app/main/category/index.html'
    model = category.Category

    def get_context_data(self, *, object_list=None, **kwargs):
        from app.models import category
        ctx = super(CategoryListView, self).get_context_data(**kwargs)
        ctx['categories'] = category.Category.objects.filter(user=self.request.user)
        return ctx


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'app/main/category/create.html'
    form_class = category.CategoryModelForm
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        self.product = form.save(commit=False)
        user = self.request.user
        self.product.user = user
        self.product.user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    from app.models.category import Category
    template_name = 'app/main/category/update.html'
    form_class = category.CategoryModelForm
    success_url = reverse_lazy('category')
    model = Category

    def form_valid(self, form):
        self.product = form.save(commit=False)
        user = self.request.user
        self.product.user = user
        self.product.user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
