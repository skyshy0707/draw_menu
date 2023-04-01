import django
django.core.management.find_commands("management/commands")
from django.shortcuts import render
# Create your views here.



def menu(request, *args, **kwargs):
    return render(
        request, 'draw_menu/menu.html', 
        { 'menu_name': kwargs.get('name') }
    )