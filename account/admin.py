# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    # views.py
    from django.shortcuts import render
    from .models import Restaurant

    def homepage(request):
        restaurant = Restaurant.objects.first()  # Fetch the first restaurant
            return render(request, 'homepage.html', {'restaurant_name': restaurant.name})
