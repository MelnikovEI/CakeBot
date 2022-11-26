from cake_orders.models import Cake, Level, Shape, Topping, Berries, Decor


def get_standard_cakes():
    """
    standard cake is a cake with a name
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


def create_cake(level, shape, topping, berries='', decor='', inscription=''):
    """
    Create a cake with given properties
    params level, shape etc.: str
    :return: id of created cake
    """
    if berries:
        berries = Berries.objects.get(title=berries)
    if decor:
        decor = Decor.objects.get(title=decor)
    cake = Cake(
        level=Level.objects.get(title=level),
        shape=Shape.objects.get(title=shape),
        topping=Topping.objects.get(title=topping),
        berries=berries,
        decor=decor,
        inscription=inscription
    )
    cake.save()
    return cake.pk
