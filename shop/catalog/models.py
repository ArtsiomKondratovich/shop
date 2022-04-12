from django.db import models


# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class SubCategories(models.Model):
    sub_category = models.CharField(max_length=100)
    category_key = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category
