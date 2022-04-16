from django.shortcuts import render
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from online_store.models import Category, SparePart
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.forms import TextInput, BooleanField


class NewCategory(CreateView):
    model = Category
    template_name = "online_store/new_category.html"
    context_name = "new-category-create"

    def form_valid(self, form):
        return super().form_valid(form)



class SparePartCreateView(CreateView):
    model = SparePart
    template_name = "online_store/add_part.html"
    fields = ["name_of_part", "description", "part_number", "price", "discount",
              "active_status"]
    widgets = {'name_of_part': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter part name'}),
                'description': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the description'}),
                'part_number': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the price'}),
                'discount': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the discount'}),
                'active_status': BooleanField(disabled={
                    'class': 'form-control',
                    'placeholder': 'Should it be active?'})
                 }

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse("store-home")


# class NewPartName(ListView):
#   model = NewPartName
#   template_name = "online_store/new_part_name.html
#   context_name = "new-part-name

#
# class SparePartListView(ListView):
#     model = SparePart
#     template_name = "online_store/home.html"
#     context_object_name = "spare-part-detail"
#     ordering = ["-discount"]
#     # paginate_by = 2


# class UserPostListView(ListView):
#     model = SparePart
#     template_name = "online_store//home.html"
#     context_object_name = "spare_part"
#     # ordering = ["-date_posted"]
#     # paginate_by = 2
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username= self.kwargs.get("username"))
#         return SparePart.objects.filter(author= user).order_by("-discount")

#
# class SparePartDetailView(DetailView):
#     model = SparePart
#
#
# class SparePartUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
#     model = SparePart
#     fields = ["name_of_part", "description", "name_of_car", "part_number", "photo", "price", "discount",
#               "active_status"]

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    #
    # def test_func(self):
    #     post = self.get_object()
    #     return post.author == self.request.user


# class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
#     model = SparePart
#
#     def form_valid(self, form):
#         # form.instance.author = self.request.user
#         return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     return post.author == self.request.user


def home(request):
    parts = SparePart.objects.order_by("-discount")
    return render(request, 'online_store/home.html', {'title': 'Welcome to our shop!', 'parts': parts})


def about(request):
    return render(request, 'online_store/about.html', {'title': 'About'})


def contacts(request):
    return render(request, 'online_store/contacts.html', {'title': 'Contact us'})


def catalogue(request):
    return render(request, 'online_store/catalogue.html', {'title': 'Catalogue'})


def login(request):
    return render(request, 'online_store/login.html', {'title': 'Login'})


def search(request):
    return render(request, 'online_store/search.html', {'title': 'Search'})


def delivery(request):
    return render(request, 'online_store/delivery.html', {'title': 'Delivery'})

