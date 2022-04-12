from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from catalog.models import SubCategories


def subcat_detail(request,pk):
    all_sub_cat = SubCategories.objects.filter(category_key_id=pk)
    print(all_sub_cat)
    context = {
        'all_sub_cat':all_sub_cat
    }
    return render(request, 'cat_detail.html', context)