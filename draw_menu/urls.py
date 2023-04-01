from django.urls import path

from . import views

app_name = 'draw_menu'

urlpatterns = [
    path('<str:name>/', views.menu, name='menu')
]