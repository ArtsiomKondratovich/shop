from .models import City


def current_city(request):
    all_cities = City.objects.all()

    request.session['the_city'] = request.GET
    context = {
        'the_city': request.session['the_city'],
        'all_cities': all_cities
    }
    return context
