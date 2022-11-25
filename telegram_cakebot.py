import os

import telebot
from telebot import types

import theme_markup

bot = telebot.TeleBot('5930122900:AAG0d2Wxllm1Z5cb6E3AFDXBxM3czITkBzc')

main_menu_message = 'Welcome to main menu'
cake_menu_message = 'This is our menu of cakes'
offers_menu_message = 'See our special offers'
custom_cake_menu_message = 'Learn more about our custom cake'
last_order_delivery_status_message = 'Here is the information about your order'
order_history_message = 'Here is your order history'
custom_cake_levels_message = 'Choose how many levels you want on the cake'
custom_cake_shape_message = 'Choose the cake shape'
custom_cake_topping_message = 'Choose the cake topping'
custom_cake_berries_message = 'Choose the cake berries'
custom_cake_decorations_message = 'Choose the cake decorations'
custom_cake_inscription_message = 'Do you want an inscription ?'
custom_cake_receive_inscription_message = 'Please enter the inscription'
prepare_order_message = 'Confirm order ?'


t_menu_cakes = [
    {
        'name': 'Red cake',
        'price': '400'
    },
    {
        'name': 'Green cake',
        'price': '600'
    },
    {
        'name': 'Blue cake',
        'price': '500'
    },
    {
        'name': 'Silver cake',
        'price': '400'
    },
    {
        'name': 'Gray cake',
        'price': '600'
    },
    {
        'name': 'Orange cake',
        'price': '500'
    },
    {
        'name': 'Velvet cake',
        'price': '400'
    },
    {
        'name': 'Yellow cake',
        'price': '600'
    },
    {
        'name': 'White cake',
        'price': '500'
    },
]

t_menu_offers = [
    {
        'name': 'Red cake',
        'price': '400'
    },
    {
        'name': 'Green cake',
        'price': '600'
    },
]
t_cake_levels = [1, 2, 3]
t_cake_shapes = ['square', 'circle', 'rectangle']
t_cake_toppings = ['white', 'caramel', 'maple', 'strawberry', 'blueberry', 'chocolate', 'none']
t_cake_berries = ['blackberry', 'raspberry', 'blueberry', 'strawberry', 'none']
t_cake_decorations = ['pistachios', 'meringue', 'hazelnut', 'pecan', 'marshmallow', 'marzipan', 'none']


def generate_markups_for_custom_cake(cake_levels, cake_shapes, cake_toppings, cake_berries, cake_decorations):
    markups = []
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    back = types.InlineKeyboardButton('Back', callback_data='back_to_previous_state')
    cake_levels_markup = types.InlineKeyboardMarkup(row_width=4)
    for cake_level in cake_levels:
        button = types.InlineKeyboardButton(str(cake_level), callback_data=f'level_{cake_level}')
        cake_levels_markup.add(button)
    cake_levels_markup.add(back_to_main)
    markups.append(cake_levels_markup)
    cake_shapes_markup = types.InlineKeyboardMarkup(row_width=3)
    for cake_shape in cake_shapes:
        button = types.InlineKeyboardButton(cake_shape.capitalize(), callback_data=f'shape_{cake_shape}')
        cake_shapes_markup.add(button)
    cake_shapes_markup.add(back, back_to_main)
    markups.append(cake_shapes_markup)
    cake_toppings_markup = types.InlineKeyboardMarkup(row_width=3)
    for cake_topping in cake_toppings:
        button = types.InlineKeyboardButton(cake_topping.capitalize(), callback_data=f'topping_{cake_topping}')
        cake_toppings_markup.add(button)
    cake_toppings_markup.add(back, back_to_main)
    markups.append(cake_toppings_markup)
    cake_berries_markup = types.InlineKeyboardMarkup(row_width=4)
    for cake_berry in cake_berries:
        button = types.InlineKeyboardButton(cake_berry.capitalize(), callback_data=f'cake_berry_{cake_berry}')
        cake_berries_markup.add(button)
    cake_berries_markup.add(back, back_to_main)
    markups.append(cake_berries_markup)
    cake_decorations_markup = types.InlineKeyboardMarkup(row_width=4)
    for cake_decoration in cake_decorations:
        button = types.InlineKeyboardButton(cake_decoration.capitalize(), callback_data=f'decoration_{cake_decoration}')
        cake_decorations_markup.add(button)
    cake_decorations_markup.add(back, back_to_main)
    markups.append(cake_decorations_markup)
    return markups


def generate_markup_for_multiple_choice(list, add_next=False, add_back=False):
    markup = types.InlineKeyboardMarkup()
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    next = types.InlineKeyboardButton('Next', callback_data='markup_next')
    back = types.InlineKeyboardButton('Back', callback_data='markup_back')
    for number, object in enumerate(list):
        button = types.InlineKeyboardButton(str(number+1), callback_data=f'menu_cake_{number+1}')
        markup.add(button)
    if add_next:
        markup.add(next)
    if add_back: 
        markup.add(back)
    markup.add(back_to_main)
    return markup

custom_cake_markups = generate_markups_for_custom_cake(t_cake_levels, t_cake_shapes, t_cake_toppings, t_cake_berries, t_cake_decorations)


@bot.message_handler(commands=['start'])
def enter_main_menu(message):
    with open('BakeCake.pdf', 'rb') as terms_of_service:
        bot.send_document(
                message.chat.id,
                document=terms_of_service,
                caption='You must accept the terms and conditions',
                reply_markup=theme_markup.get_start_markup()
            )

state = 'pending'

@bot.message_handler(content_types=['text'])
def process_answer(message):
    global state
    if state == 'adding_inscription':
        print(f'The inscription is: {message.text}')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global state
    if call.message:
        if call.data == 'back_to_main':
            state = 'main'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            with open(os.path.join('images', 'cake_main.png'), 'rb') as cake_picture:
                bot.send_photo(call.message.chat.id, cake_picture, caption=main_menu_message, reply_markup=theme_markup.get_main_markup())
        
        if call.data == 'see_cake_menu':
            state = 'menu'
            menu_page = 0
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, cake_menu_message, reply_markup=generate_markup_for_multiple_choice(t_menu_cakes))
            if call.data == 'next':
                menu_page = menu_page + 1
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=[menu_page])
            if call.data == 'back':
                menu_page = menu_page - 1

        if call.data == 'see_offers':
            state = 'offers'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, offers_menu_message, reply_markup=generate_markup_for_multiple_choice(t_menu_offers))

        if call.data == 'custom_cake_about':
            state = 'custom_cake'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, custom_cake_menu_message, reply_markup=theme_markup.get_custom_cake_about_markup())

        if call.data == 'last_order_delivery_status':
            state = 'last_order_status'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, last_order_delivery_status_message, reply_markup=theme_markup.get_last_order_delivery_status_markup())

        if call.data == 'see_history':
            state = 'order_history'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, order_history_message, reply_markup=theme_markup.get_history_markup())

        if call.data == 'custom_cake_start':
            state = 'choosing_cake_levels'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_levels_message, reply_markup=custom_cake_markups[0])

        if state == 'choosing_cake_levels':
            if 'level' in call.data:
                print(call.data.split('_')[1])
                state = 'choosing_cake_shapes'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_shape_message, reply_markup=custom_cake_markups[1])

        if state == 'choosing_cake_shapes':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_levels'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_levels_message, reply_markup=custom_cake_markups[0])
            if 'shape' in call.data:
                print(call.data.split('_')[1])
                state = 'choosing_cake_toppings'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_topping_message, reply_markup=custom_cake_markups[2])

        if state == 'choosing_cake_toppings':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_shapes'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_shape_message, reply_markup=custom_cake_markups[1])
            if 'topping' in call.data:
                print(call.data.split('_')[1])
                state = 'choosing_cake_berries'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_berries_message, reply_markup=custom_cake_markups[3])

        if state == 'choosing_cake_berries':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_toppings'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_topping_message, reply_markup=custom_cake_markups[2])
            if 'cake_berry_' in call.data:
                print(call.data.split('_')[2])
                state = 'choosing_cake_decorations'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_decorations_message, reply_markup=custom_cake_markups[4])

        if state == 'choosing_cake_decorations':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_berries'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_topping_message, reply_markup=custom_cake_markups[3])
            if 'decoration' in call.data:
                print(call.data.split('_')[1])
                state = 'choosing_cake_inscription'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_inscription_message, reply_markup=theme_markup.get_custom_cake_inscription_markup())

        if state == 'choosing_cake_inscription':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_decorations'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_decorations_message, reply_markup=custom_cake_markups[4])
            if call.data == 'add_inscription':
                state = 'adding_inscription'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_receive_inscription_message)
            if call.data == 'no_inscription':
                state == 'preparing_order'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=prepare_order_message)

        

bot.polling()