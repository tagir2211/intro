import inspect
from threading import Thread

import requests


def introspection_info(obj):
    """  - Тип объекта.
      - Атрибуты объекта.
      - Методы объекта.
      - Модуль, к которому объект принадлежит.
      - Другие интересные свойства объекта, учитывая его тип (по желанию)."""

    info = {}
    info['type'] = type(obj)
    if hasattr(obj, '__name__'):
        info['name'] = obj.__name__
    info['all_atributs'] = {}

    classes = []
    for attrs_name in dir(obj):
        attr = type(getattr(obj, attrs_name))
        if attr not in classes:
            classes.append(attr)
    for class_ in classes:
        info['all_atributs'][class_.__name__] = []

    for atrs in dir(obj):
        for class_ in classes:
            if type(getattr(obj, atrs)) == class_:
                info['all_atributs'][class_.__name__].append(atrs)
    info['methods'] = []
    for atrs in dir(obj):
        if callable(getattr(obj, atrs)):
            info['methods'].append(atrs)
    info['moudle'] = inspect.getmodule(obj)
    print(info)


introspection_info(requests)
