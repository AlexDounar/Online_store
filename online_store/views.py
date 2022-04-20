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
    context_name = "category-create"
    fields = ["category_name"]

    def form_valid(self, form):
        return super().form_valid(form)


class SparePartCreateView(CreateView):
    model = SparePart
    template_name = "online_store/sparepart_form.html"
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
        # form.instance.id = self.request.id
        return super().form_valid(form)

    def get_queryset(self):
        part = get_object_or_404(SparePart, id=self.kwargs.get("id"))
        return SparePart.objects.all()


# a view, that shows the detail information of a certain part

class SparePartListView(ListView):
    model = SparePart
    template_name = "online_store/sparepart_detail.html"
    context_object_name = "spare-part-detail"
    ordering = ["-discount"]
    # ordering = ["-date_posted"]

    def get_queryset(self):
        part = get_object_or_404(SparePart, id=self.kwargs.get("id"))
        return SparePart.objects.all()


# a view, that will show the details of a spare part

# class SparePartDetailView(DetailView):
#     model = SparePart
#     parts = SparePart.objects.all()
    # def get_queryset(self):
    #     part = get_object_or_404(SparePart, name_of_part=self.kwargs.get('id'))
    #     return render('online_store/sparepart_detail.html', {'title': 'Parts we have for sale:', 'parts': part})


def parts_detail(request, part_id):
    part = SparePart.objects.get(pk=part_id)
    return render(request, "online_store/sparepart_detail.html", {"part": part})


def home(request):
    parts = SparePart.objects.order_by("-discount")
    return render(request, 'online_store/home.html', {'title': 'Welcome to our shop!', 'parts': parts})


def about(request):
    return render(request, 'online_store/about.html', {'title': 'About'})


def contacts(request):
    return render(request, 'online_store/contacts.html', {'title': 'Contact us'})


def catalogue(request):
    parts = SparePart.objects.all()
    return render(request, 'online_store/catalogue.html', {'title': 'Parts we have for sale:', 'parts': parts})


def login(request):
    return render(request, 'online_store/login.html', {'title': 'Login'})


def search(request):
    if request.method == "POST":
        result = request.POST['result']
        parts_found = SparePart.objects.filter(description__contains=result)
        return render(request, 'online_store/search_results.html', {
            'result': result,
            'parts_found': parts_found
            })
    else:
        return render(request, 'online_store/search_results.html', {})


def delivery(request):
    return render(request, 'online_store/delivery.html', {'title': 'Delivery'})

