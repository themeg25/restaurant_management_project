# views.py
from django.conf import settings
from django.shortcuts import render

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE_NUMBER
        return render(request, 'homepage.html', {'phone_number': phone_number})
        
                                                                                         