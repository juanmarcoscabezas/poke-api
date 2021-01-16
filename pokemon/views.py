from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Pokemon

from django.shortcuts import redirect

def view_404(request, exception=None):
    redirect_url = request.META['PATH_INFO']
    return redirect('/?redirect={}'.format(redirect_url))

def index(request):
    context = {}
    pokemon_name = request.GET.get('pokemon_name')
    page_number = request.GET.get('page')
    error_message = None

    if pokemon_name is not None and pokemon_name != '':
        pokemon_detail = Pokemon.objects.filter(name__contains=pokemon_name)[:1]
        if len(pokemon_detail) == 0:
            error_message = 'Pokemon not found'
        context['pokemon_detail'] = pokemon_detail
    
    if page_number is None or page_number == '':
        page_number = 1

    pokemon_list = Pokemon.objects.all().order_by('id')
    paginator = Paginator(pokemon_list, 6)
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    context['pokemon_name'] = pokemon_name
    context['error_message'] = error_message
    return render(request, 'pokemon/index.html', context=context)
