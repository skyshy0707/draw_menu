import json
from ..models import Point

def menu_validator(scheme):
    menu_names = Point.objects.all().values_list('name', flat=True)
    
    new_names = []
    for menu in scheme:
        menu_name = menu.get('name')
        points = menu.get('points')
        new_names.append(menu_name)

        assert menu_name not in menu_names
        assert isinstance(menu_name, str)
        assert isinstance(points, (list, type(None)))
        if points: new_names.extend(menu_validator(points))

    assert len(new_names) == len(set(new_names))
    return new_names

def menu_validate(path_to_json):
    try:
        scheme = json.load(open(path_to_json, encoding='utf-8', mode='r'))
        menu_validator(scheme)
    except json.JSONDecodeError:
        raise ValueError("Некорректный формат json")
    except AssertionError:
        raise ValueError("Некорректный формат данных json") 
    except PermissionError:
        raise PermissionError("Недостаточно прав")
    except FileNotFoundError:
        raise FileNotFoundError("Неверный путь")
    return scheme



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
                            {"name": "Центральный (Наб. Челны)"},
                            {"name": "Азьмушкино"},
                            {"name": "Большая Шильна"}
                        ]
                    },
                    {
                        "name": "Нижнекамск",
                        "points": [
                            {"name": "Центральный (Нижнекамск)"},
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
                            {"name": "Московский (Чебоксары)"},
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
                            {"name": "Центральный (Канаш)"},
                            {"name": "Восточный (Канаш)"}
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
                            {"name": "Калининский (Уфа)"},
                            {"name": "Ленинский (Уфа)"},
                            {"name": "Кировский (Уфа)"},
                            {"name": "Октябрьский"},
                            {"name": "Орджоникидзевский"},
                            {"name": "Советский (Уфа)"}
                        ]
                    },
                    {
                        "name": "Стерлитамак",
                        "points": [
                            {"name": "Ленинский (Стерлитамак)"},
                            {"name": "Кутузовский"},
                            {"name": "Солнечный"},
                            {"name": "Старый Город"},
                            {"name": "ВТС"},
                        ]
                    },
                    {
                        "name": "Салават",
                        "points": [
                            {"name": "Центральный (Салават)"},
                            {"name": "Северный"},
                            {"name": "Мусино"},
                        ]
                    },
                    {
                        "name": "Нефтекамск",
                        "points": [
                            {"name": "Центральный (Нефтекамск)"},
                            {"name": "Марино"},
                            {"name": "Ташниково"},
                        ]
                    },
                    {
                        "name": "Октябрьский (город)",
                        "points": [
                            {"name": "Центральный (г. Октябрьский - [02])"},
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
                            { "name": "Центральный (Омск)" },
                            { "name": "Октябрьский (Омск)" },
                            { "name": "Ленинский (Омск)" },
                            { "name": "Кировский (Омск)" },
                            { "name": "Советский (Омск)" },
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
                            { "name": "Советский (Томск)" },
                            { "name": "Октябрьский (Томск)" },
                            { "name": "Ленинский (Томск)" },
                            { "name": "Кировский (Томск)" },
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
                            { "name": "Центральный (Стрежевой)" }
                        ]
                    }
                ]
            }
        ]
    }
]
#menu_validator(list_)

#menu_validate('locations.json')
#js = json.load(open('locations.json', encoding ='utf-8', mode ='r'))
#print(js)