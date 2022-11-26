from django.contrib import admin

from cake_orders.models import Level, Shape, Cake, Topping, Berries, Decor, Client

admin.site.register(Level)
admin.site.register(Shape)
admin.site.register(Topping)
admin.site.register(Berries)
admin.site.register(Decor)
admin.site.register(Cake)
admin.site.register(Client)
