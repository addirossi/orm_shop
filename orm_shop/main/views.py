from django.http import Http404
from django.shortcuts import render

from main.models import Car


def cars_list_view(request):
    # получите список авто
    queryset = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': queryset})


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404('Car not found')
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})


# def sales_by_car(request, car_id):
