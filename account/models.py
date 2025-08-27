# views.py
from django.shortcuts import render

def menu_view(request):
    # Hardcoded menu items for simplicity
        menu_items = [
                {'name': 'Burger', 'description': 'Juicy beef burger', 'price': 8.99},
                        {'name': 'Pizza', 'description': 'Cheese pizza with veggies', 'price': 10.99},
                                {'name': 'Salad', 'description': 'Fresh garden salad', 'price': 6.99},
                                    ]
                                        return render(request, 'menu.html', {'menu_items': menu_items})                                                                            quantity = models.PositiveIntegerField(default=1)