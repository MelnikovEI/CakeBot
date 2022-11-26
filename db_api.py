from cake_orders.models import Cake, Level, Shape, Topping, Berries, Decor


def get_standard_cakes():
    """
    standard cake - a cake with a name
    :return: a list of standard cakes {id, title, price}
    """
    return list(Cake.objects.exclude(title='').values('id', 'title', 'price'))


def get_levels():
    return list(Level.objects.values_list('title', flat=True))


def get_shapes():
    return list(Shape.objects.values_list('title', flat=True))


def get_toppings():
    return list(Topping.objects.values_list('title', flat=True))


def get_berries():
    return list(Berries.objects.values_list('title', flat=True))


def get_decors():
    return list(Decor.objects.values_list('title', flat=True))

