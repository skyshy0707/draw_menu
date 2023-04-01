from django.core.management.base import BaseCommand

from ..validator import menu_validate
from ...models import Point

class Command(BaseCommand):

    help = "Создаёт новое меню по json"

    def add_arguments(self, parser):
        parser.add_argument(
            "path_to_json", 
            type=menu_validate, 
            help="путь к файлу json, определяющий меню"
        )
    
    def create_menu(self, scheme):
        menus = []
        for menu in scheme:
            menu_obj, _ = Point.objects.get_or_create(name=menu.get("name"))
            if menu.get("points"):
                points = self.create_menu(menu["points"])
                menu_obj.points.add(*points)
            menus.append(menu_obj)
        return menus

    def handle(self, path_to_json, *args, **kwargs):
        self.create_menu(path_to_json)