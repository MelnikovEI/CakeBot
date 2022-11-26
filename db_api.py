import datetime

from cake_orders.models import Cake, Level, Shape, Topping, Berries, Decor, Client, Order


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


def add_account(tg_account, pd_read=False):
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


def get_pd_status(client_id):
    """Checks PD status"""
    try:
        account = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return False
    else:
        return account.pd_read


def add_order(client_id, client_delivery_datetime: datetime, delivery_address, is_urgent, comment=''):
    """Creates new order"""
    client = Client.objects.get(id=client_id)
    new_order = Order(client=client, client_delivery_datetime=client_delivery_datetime,
                      delivery_address=delivery_address, is_urgent=is_urgent, comment=comment)
    new_order.save()
    return new_order.pk


def add_cake_to_order(order_id, cake_id):
    """Adds cake to order"""
    order = Order.objects.get(id=order_id)
    cake = Cake.objects.get(id=cake_id)
    order.cake.add(cake)
    return order.pk


def get_orders(client_id):
    orders = Order.objects.filter(client__id=client_id)
    return list(orders.values())


if __name__ == '__main__':
    print(get_orders(4))
    #print(add_cake_to_order(2, 11))
    print(add_account('@MelnikovEI11'))
    #print(add_order(4, '2022-12-01', 'Адрес доставки', False))
    #print(get_pd_status('@MelnikovEI11'))
    #new_client = Client(tg_account='@MelnikovEI')

    #print(new_client.pk, new_client.tg_account, new_client.pd_read)
