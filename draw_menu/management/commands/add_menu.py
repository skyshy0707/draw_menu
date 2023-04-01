from django.core.management.base import BaseCommand

from ..validator import menu_validate
from ...models import Point

class Command(BaseCommand):

    help = "Creates a new menu"

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


"""
def add(list_):
    struct = []
    for item in list_:
        new_item = { 'name': item["name"] }
        if item.get("points"):
            points = add(item["points"])
            new_item["points"] = points
        struct.append(new_item)
    return struct
            
list_ = [
    {
        "name": "Булгария",
        "points": [
            {
                "name": "Марий Эл",
                "points": [
                    {
                        "name": "Йошкар-Ола",
                        "points": [
                            { "name": "Сомбатей" },
                            { "name": "Чихайдарово"},
                            { "name": "Машиностроитель"},
                            { "name": "Оршанский" }
                        ]
                    },
                    {
                        "name": "Волжск",
                        "points": [
                            {"name": "Заря"},
                            {"name": "Центральный"}
                        ]
                    }
                ]
            },
            {
                "name": "Татарстан",
                "points": [
                    {
                        "name": "Казань",
                        "points": [
                            {"name": "Вахитовский"},
                            {"name": "Авиастроительный"},
                            {"name": "Нови-Савиновский"},
                            {"name": "Кировский"},
                            {"name": "Приволжский"},
                            {"name": "Московский"},
                            {"name": "Советский"}
                        ]
                    },
                    {
                        "name": "Набережные Челны",
                        "points": [
                            {"name": "Автозаводский"},
                            {"name": "Комсомольский"},
                            {"name": "Центральный"},
                            {"name": "Азьмушкино"},
                            {"name": "Большая Шильна"}
                        ]
                    },
                    {
                        "name": "Нижнекамск",
                        "points": [
                            {"name": "Центральный"},
                            {"name": "Строителей"},
                            {"name": "Промзона"},
                            {"name": "Афанасово"}
                        ]
                    },
                    {
                        "name": "Альтемьевск",
                        "points": [
                            {"name": "Красноармейский"},
                            {"name": "Урсала"},
                            {"name": "ДОСААФ"}
                        ]
                    }
                ]
            },
            {
                "name": "Чувашия",
                "points": [
                    {
                        "name": "Чебоксары",
                        "points": [
                            {"name": "Московский"},
                            {"name": "Калининский"},
                            {"name": "Ленинский"},
                            {"name": "Заволжье"},
                            {"name": "Ягудары"}
                        ]
                    },
                    {
                        "name": "Новочебоксарск",
                        "points": [
                            {"name": "Восточный"},
                            {"name": "Южный"},
                            {"name": "Западный"}
                        ]
                    },
                    {
                        "name": "Канаш",
                        "points": [
                            {"name": "Центральный"},
                            {"name": "Восточный"}
                        ]
                    }
                ]
            }, 
            {
                "name": "Башкортостан",
                "points": [
                    {
                        "name": "Уфа",
                        "points": [
                            {"name": "Дёмский"},
                            {"name": "Калининский"},
                            {"name": "Ленинский"},
                            {"name": "Кировский"},
                            {"name": "Октябрьский"},
                            {"name": "Орджоникидзевский"},
                            {"name": "Советский"}
                        ]
                    },
                    {
                        "name": "Стерлитамак",
                        "points": [
                            {"name": "Ленинский"},
                            {"name": "Кутузовский"},
                            {"name": "Солнечный"},
                            {"name": "Старый Город"},
                            {"name": "ВТС"},
                        ]
                    },
                    {
                        "name": "Салават",
                        "points": [
                            {"name": "Центральный"},
                            {"name": "Северный"},
                            {"name": "Мусино"},
                        ]
                    },
                    {
                        "name": "Нефтекамск",
                        "points": [
                            {"name": "Центральный"},
                            {"name": "Марино"},
                            {"name": "Ташниково"},
                        ]
                    },
                    {
                        "name": "Октябрьский",
                        "points": [
                            {"name": "Центральный"},
                            {"name": "Первомайский"},
                            {"name": "Верхнее Зайтово"},
                        ]
                    }
                ]
            }
        ]
    },
    {
        "name": "Селькупия",
        "points": [
            {
                "name": "Омская область",
                "points": [
                    { 
                        "name": "Омск",
                        "points": [
                            { "name": "Центральный" },
                            { "name": "Октябрьский" },
                            { "name": "Ленинский" },
                            { "name": "Кировский" },
                            { "name": "Советский" },
                            { "name": "Дружино" }
                        ]
                    },
                    {
                        "name": "Тара"
                    }
                ]
            },
            {
                "name": "Томская область",
                "points": [
                    {
                        "name": "Томск",
                        "points": [
                            { "name": "Советский" },
                            { "name": "Октябрьский" },
                            { "name": "Ленинский" },
                            { "name": "Кировский" },
                            { "name": "Чёрная Речка" }
                        ]
                    }, 
                    {
                        "name": "Северск",
                        "points": [
                            { "name": "Новый" },
                            { "name": "Старая территория" },
                        ]
                    },
                    {
                        "name": "Стрежевой",
                        "points": [
                            { "name": "Центральный" }
                        ]
                    }
                ]
            }
        ]
    }
]

res = add(list_)

print("res", res)
"""