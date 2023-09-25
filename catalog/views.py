from django.shortcuts import render
from .models import Car


# Create your views here.
def content(request):
    car_obj = Car.objects.all()
    return render(request, 'catalog/content.html', {'car_obj': car_obj})
