from django import template
from django.forms.models import model_to_dict

from ..models import Point

register = template.Library()


@register.filter(name="lookup")
def lookup(a_list, index):
    return a_list[index]

@register.inclusion_tag('draw_menu/draw_menu.html')
def draw_menu(name):
    query = """
    WITH RECURSIVE points AS (
        SELECT draw_menu_point.*, 0 AS relative_depth
        FROM draw_menu_point
        WHERE name = %s

        UNION ALL

        SELECT draw_menu_point.*, points.relative_depth - 1
        FROM draw_menu_point,points
        WHERE draw_menu_point.id = points.menu_id
    )
    SELECT id, name, relative_depth
    FROM points 
    ORDER BY relative_depth;
    """
    points = list(Point.objects.raw(query, [name]))
    expanded_names = list(map(
        lambda x: model_to_dict(x)['name'], points)
    )
    return { 
        'expanded_names': expanded_names,
        'index': 0,
        'node': points[0] if points else None
    }