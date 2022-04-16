from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, SparePartSubCategory, SparePart, PartImage


admin.site.register(Category)
admin.site.register(SparePartSubCategory)
admin.site.register(SparePart)
admin.site.register(PartImage)


