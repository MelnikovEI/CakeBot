from bake_cake import setup

setup()
import db_api

"""Примеры применения функций"""

print('id клиента: ', db_api.add_client('@MelnikovEI11'))
print()
print('Все заказы клиента 4: ', db_api.get_orders(4))
print()
print('Все стандартные торты (у них есть название): ', db_api.get_standard_cakes())
print()
print('Все заказы клмиента №4: ', db_api.get_orders(4))
print()
print('Создан новый заказ № ', db_api.add_order(4, db_api.get_current_datetime(), db_api.get_estimate_delivery_datetime(True), 'Мой адрес, никому не скажу', True, 'Мой пёс - получатель', 'Мой коммент', 'Принят'))
print()
print('Создан новый торт № ', db_api.create_cake('3', 'Square', 'Milk chocolate', 'No berries', 'No decor'))
print()
print('Статус клиента прочтения PD: ', db_api.get_pd_status(4))
print()
print('Торт добавлен в заказ № ', db_api.add_cake_to_order(11, 11))
