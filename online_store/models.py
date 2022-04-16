from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.utils import dateparse
from django.contrib.auth.models import User


# a class that is the model for a new category creation

class Category(models.Model):
    category_name = models.CharField(max_length= 20)

    def __str__(self):
        return self.category_name


# a class that is the model for a new spare part sub category

class SparePartSubCategory(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     name_of_part = models.TextField(max_length=20)
     model_of_auto = models.CharField(max_length=50)

     def __str__(self):
         return str(self.name_of_part)


# a model for a new spare part addition

class SparePart(models.Model):
    name_of_part = models.ForeignKey(SparePartSubCategory, on_delete=models.CASCADE)
    description = models.TextField()
    part_number = models.CharField(default=None, max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField()
    active_status = models.BooleanField(default=True)
    sold_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name_of_part)

    def get_absolute_url(self):
        return reverse("store-home")


# a model for saving photos for a spare part as redirection to a storage place by article of a part

class PartImage(models.Model):
    id_of_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    image = models.ImageField(default='test.jpg', upload_to="profile_pics")

