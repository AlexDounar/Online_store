from .models import Category, SparePart, SparePartSubCategory
from django.forms import ModelForm, TextInput


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category name"]


class SparePartForm(ModelForm):
    class Meta:
        model = SparePart
        fields = ['name_of_part', 'description', 'part_number', 'price', 'discount', 'active_status']