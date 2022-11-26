from cake_orders.models import Cake, Level, Shape, Topping, Berries, Decor, Client


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
    :return: None
    """
    try:
        account = Client.objects.get(tg_account=tg_account)
    except Client.DoesNotExist:
        new_client = Client(tg_account=tg_account, pd_read=pd_read)
        new_client.save()
    else:
        account.pd_read = pd_read
        account.save()


def get_pd_status(tg_account):
    try:
        account = Client.objects.get(tg_account=tg_account)
    except Client.DoesNotExist:
        return False
    else:
        return account.pd_read



#print(add_account('@MelnikovEI11'))
print(get_pd_status('@MelnikovEI11'))
#new_client = Client(tg_account='@MelnikovEI')

#print(new_client.pk, new_client.tg_account, new_client.pd_read)
