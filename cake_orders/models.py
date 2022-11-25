from django.db import models


class Level(models.Model):
    title = models.PositiveSmallIntegerField('level')
    price = models.PositiveIntegerField('price')

    def __str__(self):
        return str(self.title)


class Shape(models.Model):
    title = models.CharField('shape', max_length=50)
    price = models.PositiveIntegerField('price')

    def __str__(self):
        return self.title


class Topping(models.Model):
    title = models.CharField('topping', max_length=50)
    price = models.PositiveIntegerField('price')

    def __str__(self):
        return self.title


class Berries(models.Model):
    title = models.CharField('berries', max_length=50)
    price = models.PositiveIntegerField('price')

    def __str__(self):
        return self.title


class Decor(models.Model):
    title = models.CharField('decor', max_length=50)
    price = models.PositiveIntegerField('price')

    def __str__(self):
        return self.title


class Inscription(models.Model):
    title = models.CharField('inscription', max_length=50)
    price = models.PositiveIntegerField('price')


class Cake(models.Model):
    title = models.CharField('name', max_length=50, blank=True)
    price = models.PositiveIntegerField('price')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='levels in cake')
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name='Shape of the cake')
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, verbose_name='Topping for the cake')
    berries = models.ForeignKey(Berries, on_delete=models.CASCADE, verbose_name='Berries for the cake', blank=True)
    decor = models.ForeignKey(Decor, on_delete=models.CASCADE, verbose_name='Decor for the cake', blank=True)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE, verbose_name='Inscription for the cake',
                                    blank=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    tg_account = models.CharField('telegram account for communication', max_length=200)
    pd_read = models.BooleanField('personal data agreement read?', default=False)


class Order(models.Model):
    cake = models.ManyToManyField(Cake, verbose_name='cakes in the order')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='client')
    comment = models.CharField('comment for order and delivery', max_length=400, blank=True)
    client_delivery_datetime = models.DateTimeField("client's date and time of the delivery")
    forecast_delivery_datetime = models.DateTimeField("client's date and time of the delivery")
    delivery_address = models.CharField('delivery address', max_length=200)
    is_urgent = models.BooleanField('is order urgent?', default=False)
    """The order is urgent if delivery period less than 24 hours"""
    price = models.PositiveIntegerField('price')
