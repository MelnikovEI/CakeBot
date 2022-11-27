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


class Cake(models.Model):
    title = models.CharField('name', max_length=50, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='levels in cake')
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name='Shape of the cake')
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, verbose_name='Topping for the cake')
    berries = models.ForeignKey(Berries, on_delete=models.CASCADE, verbose_name='Berries for the cake', null=True,
                                blank=True)
    decor = models.ForeignKey(Decor, on_delete=models.CASCADE, verbose_name='Decor for the cake', null=True, blank=True)
    inscription = models.CharField('inscription', max_length=100, blank=True)
    price = models.FloatField('price of the cake', null=True, blank=True)

    def calc_price(self):
        price = self.level.price + self.shape.price + self.topping.price
        if self.berries:
            price += self.berries.price
        if self.decor:
            price += self.decor.price
        if self.inscription:
            price += 500
        return price

    def __str__(self):
        return f'{self.id} {self.title}'

    def save(self, *args, **kwargs):
        self.price = self.calc_price()
        super(Cake, self).save(*args, **kwargs)


class Client(models.Model):
    tg_account = models.CharField('telegram account for communication', max_length=200, unique=True)
    pd_read = models.BooleanField('personal data agreement read?', default=False)

    def __str__(self):
        return self.tg_account


class Order(models.Model):
    cake = models.ManyToManyField(Cake, verbose_name='cakes in the order')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='client')
    comment = models.CharField('comment for order and delivery', max_length=400, blank=True)
    delivery_datetime = models.DateTimeField("date and time of the delivery")
    delivery_address = models.CharField('delivery address', max_length=200)
    is_urgent = models.BooleanField('is order urgent?', default=False)
    """The order is urgent if delivery period less than 24 hours"""
    @property
    def price(self):
        return self.cake.price * (1 + 0.2 * self.is_urgent)
    status = models.CharField('Status of the order', max_length=50)
