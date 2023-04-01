import json
from ..models import Point

def menu_validator(scheme):
    """
    Валидатор json структуры древовидных меню.

    Проверяет типы данных в структуре в соответствии с 
    настройками БД.
    """
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
    """
    Метод для валидации меню, описанных в json.
    """
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