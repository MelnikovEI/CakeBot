from bake_cake import setup

setup()
import db_api

"""Примеры применения функций"""

print(db_api.add_client('@MelnikovEI11'))
print(db_api.get_orders(4))
print(db_api.get_standard_cakes())
print(db_api.get_orders(4))
print(db_api.add_order(4, '2022-01-01', 'Мой адрес, никому не скажу', True, 'Мой коммент', 'Принят'))
print(db_api.create_cake('3', 'Square', 'Milk chocolate', 'No berries', 'No decor'))
print(db_api.get_pd_status(4))
print(db_api.add_cake_to_order(8, 15))