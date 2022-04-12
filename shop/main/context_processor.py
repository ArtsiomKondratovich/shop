from .models import City
from catalog.models import SubCategories, Categories


def current_city(request):
    all_cities = City.objects.all()

    request.session['the_city'] = request.GET
    context = {
        'the_city': request.session['the_city'],
        'all_cities': all_cities
    }
    return context


def catalog(request):
    subcat = SubCategories.objects.all()
    cat = Categories.objects.all()
    context = {'subcat': subcat,
               'cat': cat
               }
    return context