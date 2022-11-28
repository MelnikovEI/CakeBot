import datetime

from cake_orders.models import (Berries, Cake, Client, Decor, Level, Order,
                                Shape, Topping)


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


def create_cake(level, shape, topping, berries, decor, inscription=''):
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


def add_client(tg_account, pd_read=False):
    """
    Creates new client and/or sets status of PD read
    :param tg_account: name of telegram account
    :param pd_read: status of PD read
    :return: client_id
    """
    try:
        account = Client.objects.get(tg_account=tg_account)
    except Client.DoesNotExist:
        new_client = Client(tg_account=tg_account, pd_read=pd_read)
        new_client.save()
        return new_client.pk
    else:
        account.pd_read = pd_read
        account.save()
        return account.pk


def get_pd_status(tg_account):
    """Checks PD status"""
    try:
        account = Client.objects.get(tg_account=tg_account)
    except Client.DoesNotExist:
        return False
    else:
        return account.pd_read


def add_order(client_id, creation_datetime: datetime, delivery_datetime: datetime, delivery_address, is_urgent, recipient_name='', comment='', status=''):
    """Creates new order"""
    client = Client.objects.get(id=client_id)
    new_order = Order(client=client, creation_datetime=creation_datetime, delivery_datetime=delivery_datetime,
                      delivery_address=delivery_address, is_urgent=is_urgent, recipient_name=recipient_name,
                      comment=comment, status=status)
    new_order.save()
    return new_order.pk


def add_cake_to_order(order_id, cake_id):
    """Adds cake to order"""
    order = Order.objects.get(id=order_id)
    cake = Cake.objects.get(id=cake_id)
    order.cake.add(cake)
    return order.pk


def get_orders(client_id):
    """get all orders of a client"""
    orders = Order.objects.filter(client__id=client_id)
    return list(orders.values('id', 'creation_datetime', 'status'))


def get_cakes(order_id):
    """get cakes from order"""
    cakes = Cake.objects.filter(order__id=order_id)
    return list(cakes.values('id', 'title', 'price'))


def get_current_datetime():
    current_time = datetime.datetime.now()
    str_time = current_time.strftime('%Y-%m-%d')
    return str_time

def get_estimate_delivery_datetime(urgent):
    if urgent:
        time = datetime.datetime.now() + datetime.timedelta(days=1)
    else:
        time = datetime.datetime.now() + datetime.timedelta(days=3)
    str_time = time.strftime('%Y-%m-%d')
    return str_time