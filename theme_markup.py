from telebot import types


def get_start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept_conditions = types.InlineKeyboardButton('Accept terms and conditions', callback_data='back_to_main')
    markup.add(accept_conditions)
    return markup


def get_main_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    see_menu = types.InlineKeyboardButton('Cake menu', callback_data='see_cake_menu')
    see_offers = types.InlineKeyboardButton('Special offers', callback_data='see_offers')
    custom_cake = types.InlineKeyboardButton('Custom cake', callback_data='custom_cake_about')
    see_last_order_delivery_status = types.InlineKeyboardButton('Check delivery status', callback_data='last_order_delivery_status')
    see_history = types.InlineKeyboardButton('Order history', callback_data='see_history')
    markup.add(see_offers, see_menu, custom_cake, see_last_order_delivery_status, see_history)
    return markup


def get_cake_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    position_1 = types.InlineKeyboardButton('1', callback_data='cake_menu_position_1')
    position_2 = types.InlineKeyboardButton('2', callback_data='cake_menu_position_2')
    position_3 = types.InlineKeyboardButton('3', callback_data='cake_menu_position_3')
    position_4 = types.InlineKeyboardButton('4', callback_data='cake_menu_position_4')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(position_1, position_2, position_3, position_4, back_to_main)
    return markup


def get_offers_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    position_1 = types.InlineKeyboardButton('1', callback_data='offer_menu_position_1')
    position_2 = types.InlineKeyboardButton('2', callback_data='offer_menu_position_2')
    position_3 = types.InlineKeyboardButton('3', callback_data='offer_menu_position_3')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(position_1, position_2, position_3, back_to_main)
    return markup


def get_custom_cake_about_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    accept = types.InlineKeyboardButton('Order a custom cake', callback_data='custom_cake_start')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(accept, back_to_main)
    return markup

 
def get_custom_cake_levels_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    level_1 = types.InlineKeyboardButton('One level', callback_data='custom_cake_level_1')
    level_2 = types.InlineKeyboardButton('Two levels', callback_data='custom_cake_level_2')
    level_3 = types.InlineKeyboardButton('Three levels', callback_data='custom_cake_level_3')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(level_1, level_2, level_3, back_to_main)
    return markup


def get_custom_cake_shape_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    square = types.InlineKeyboardButton('Square', callback_data='custom_cake_square')
    circle = types.InlineKeyboardButton('Circle', callback_data='custom_cake_circle')
    rectangle = types.InlineKeyboardButton('Rectangle', callback_data='custom_cake_rectangle')
    back_to_custom_cake_levels = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_levels')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    markup.add(square, circle, rectangle, back_to_custom_cake_levels, back_to_main)
    return markup


def get_custom_cake_topping_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    white_syrup = types.InlineKeyboardButton('White', callback_data='white_syrup')
    caramel_syrup = types.InlineKeyboardButton('Caramel', callback_data='caramel_syrup')
    maple_syrup = types.InlineKeyboardButton('Maple', callback_data='maple_syrup')
    strawberry_syrup = types.InlineKeyboardButton('Strawberry', callback_data='strawberry_syrup')
    blueberry_syrup = types.InlineKeyboardButton('Blueberry', callback_data='blueberry_syrup')
    milk_chocolate = types.InlineKeyboardButton('Chocolate', callback_data='milk_chocolate')
    no_topping = types.InlineKeyboardButton('No topping', callback_data='no_topping')
    back_to_custom_cake_shape = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_shape')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    markup.add(white_syrup, caramel_syrup, maple_syrup, strawberry_syrup, blueberry_syrup, milk_chocolate, no_topping, back_to_custom_cake_shape, back_to_main)
    return markup


def get_custom_cake_berries_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    blackberry = types.InlineKeyboardButton('Blackberry', callback_data='blackberry_berry')
    raspberry = types.InlineKeyboardButton('Raspberry', callback_data='raspberry_berry')
    blueberry = types.InlineKeyboardButton('Blueberry', callback_data='blueberry_berry')
    strawberry = types.InlineKeyboardButton('Strawberry', callback_data='strawberry_berry')
    no_berry = types.InlineKeyboardButton('Skip', callback_data='no_berry')
    back_to_custom_cake_topping = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_topping')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    finish = types.InlineKeyboardButton('Finish', callback_data='finish_customization')
    markup.add(blackberry, raspberry, blueberry, strawberry, no_berry, finish, back_to_custom_cake_topping, back_to_main)
    return markup


def get_custom_cake_decorations_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    pistachios = types.InlineKeyboardButton('Pistachios', callback_data='pistachios_decoration')
    meringue = types.InlineKeyboardButton('Meringue', callback_data='meringue_decoration')
    hazelnut = types.InlineKeyboardButton('Hazelnut', callback_data='hazelnut_decoration')
    pecan = types.InlineKeyboardButton('Pecan', callback_data='pecan_decoration')
    marshmallow = types.InlineKeyboardButton('Marshmallow', callback_data='marshmallow_decoration')
    marzipan = types.InlineKeyboardButton('Marzipan', callback_data='marzipan_decoration')
    no_decoration = types.InlineKeyboardButton('Skip', callback_data='no_decoration')
    back_to_custom_cake_berries = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_berries')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    finish = types.InlineKeyboardButton('Finish', callback_data='finish_customization')
    markup.add(pistachios, meringue, hazelnut, pecan, marshmallow, marzipan, no_decoration, finish, back_to_custom_cake_berries, back_to_main)
    return markup


def get_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=4)
    add_inscription = types.InlineKeyboardButton('Add', callback_data='inscription')
    no_inscription = types.InlineKeyboardButton('Skip', callback_data='no_inscription')
    back_to_custom_cake_decorations = types.InlineKeyboardButton('Back', callback_data='back_to_custom_cake_decorations')
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    finish = types.InlineKeyboardButton('Finish', callback_data='finish_customization')
    markup.add(add_inscription, no_inscription, finish, back_to_custom_cake_decorations, back_to_main)
    return markup


def get_writing_custom_cake_inscription_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    cancel_inscription = types.InlineKeyboardButton('Cancel', callback_data='cancel_inscription')
    markup.add(cancel_inscription)
    return markup


def get_last_order_delivery_status_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(back_to_main)
    return markup
    

def get_history_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    repeat_last_order = types.InlineKeyboardButton('Repeat last order', callback_data='repeat_last_order')
    repeat_select_order = types.InlineKeyboardButton('Repeat specific order', callback_data='repeat_specific_order')
    back_to_main = types.InlineKeyboardButton('Back to main menu', callback_data='back_to_main')
    markup.add(repeat_last_order, repeat_select_order, back_to_main)
    return markup