import os

import telebot
from telebot import types
from bake_cake import setup

import theme_markup

setup()

import db_api

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
prepare_custom_order_message = 'Confirm order ?'

t_menu_orders = [
    {
        'id': 1,
        'date': '26.11.2022',
        'time': '14:00',
        'cake_id': '5',
        'status': 'Completed',
    },
    {
        'id': 2,
        'date': '25.11.2022',
        'time': '15:00',
        'cake_id': '3',
        'status': 'Completed',
    },
    {
        'id': 3,
        'date': '25.11.2022',
        'time': '15:00',
        'cake_id': '2',
        'status': 'Canceled',
    }
]



t_menu_cakes = [
    {
        'id': 1,
        'name': 'Red cake',
        'price': '400'
    },
    {
        'id': 2,
        'name': 'Green cake',
        'price': '600'
    },
    {
        'id': 3,
        'name': 'Blue cake',
        'price': '500'
    },
    {   
        'id': 4,
        'name': 'Silver cake',
        'price': '400'
    },
    {
        'id': 5,
        'name': 'Gray cake',
        'price': '600'
    },
    {
        'id': 6,
        'name': 'Orange cake',
        'price': '500'
    },
    {
        'id': 7,
        'name': 'Velvet cake',
        'price': '400'
    },
    {
        'id': 8,
        'name': 'Yellow cake',
        'price': '600'
    },
    {
        'id': 9,
        'name': 'White cake',
        'price': '500'
    },
]

t_menu_offers = [
    {
        'id': 1,
        'name': 'Red cake',
        'price': '400'
    },
    {
        'id': 2,
        'name': 'Green cake',
        'price': '600'
    },
]


t_cake_levels = [1, 2, 3]
t_cake_shapes = ['square', 'circle', 'rectangle']
t_cake_toppings = ['white', 'caramel', 'maple', 'strawberry', 'blueberry', 'chocolate', 'none']
t_cake_berries = ['blackberry', 'raspberry', 'blueberry', 'strawberry', 'none']
t_cake_decorations = ['pistachios', 'meringue', 'hazelnut', 'pecan', 'marshmallow', 'marzipan', 'none']


def get_split_list(list, chunk_size):
    split_list = []
    for i in range(0, len(list), chunk_size):
        split_list.append(list[i:i + chunk_size])
    return split_list


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




def generate_markup_for_multiple_choice(list):
    markups = []
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    max_choices = 5
    split_lists = get_split_list(list, max_choices)
    for split_list in split_lists:
        markup = types.InlineKeyboardMarkup()
        for number, split_list_item in enumerate(split_list):
            button = types.InlineKeyboardButton(str(number+1), callback_data=f'list_position_id_{split_list_item.get("id")}')
            markup.add(button)
        if split_lists.index(split_list) > 0:
            back = types.InlineKeyboardButton('Back', callback_data=f'markup_back_from_{split_lists.index(split_list)}')
            markup.add(back)
        if not split_list == split_lists[-1]:
            next = types.InlineKeyboardButton('Next', callback_data=f'markup_next_from_{split_lists.index(split_list)}')
            markup.add(next)
        markup.add(back_to_main)
        markups.append(markup)
    return markups 

custom_cake_markups = generate_markups_for_custom_cake(t_cake_levels, t_cake_shapes, t_cake_toppings, t_cake_berries, t_cake_decorations)
cake_menu_markup = generate_markup_for_multiple_choice(t_menu_cakes)
offers_menu_markup = generate_markup_for_multiple_choice(t_menu_offers)


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
        state = 'confirming_custom_order'
        inscription = message.text
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The inscription is: {inscription}. Confirm ?', reply_markup=theme_markup.get_confirm_custom_order_markup())
    if state == 'entering_delivery_address':
        state = 'confirming_address'
        address = message.text
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The address is: {address}. Confirm ?', reply_markup=theme_markup.get_address_confirm_markup())
    if state == 'entering_receiver':
        state = 'confirming_receiver'
        receiver = message.text
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The receiver is: {receiver}. Confirm ?', reply_markup=theme_markup.get_receiver_confirm_markup())
    if state == 'entering_comment':
        state = 'confirming_comment'
        comment = message.text
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The comment is: {comment}. Confirm ?', reply_markup=theme_markup.get_comment_confirm_markup())
            

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global state
    if call.message:
        if call.data == 'back_to_main':
            state = 'main'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            with open(os.path.join('images', 'cake_main.png'), 'rb') as cake_picture:
                bot.send_photo(call.message.chat.id, cake_picture, caption=main_menu_message, reply_markup=theme_markup.get_main_markup())

# menu
        if call.data == 'see_cake_menu':
            state = 'menu'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, cake_menu_message, reply_markup=cake_menu_markup[0])
        if state == 'menu':
            if 'markup_next_from' in call.data:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=cake_menu_markup[int(call.data.split('_')[3])+1])
            if 'markup_back_from' in call.data:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=cake_menu_markup[int(call.data.split('_')[3])-1])
            if 'list_position_id' in call.data:
                print(call.data)

# delivery status
        if call.data == 'last_order_delivery_status':
            state = 'last_order_status'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, last_order_delivery_status_message, reply_markup=theme_markup.get_last_order_delivery_status_markup())

# history 
        if call.data == 'see_history':
            state = 'order_history'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, order_history_message, reply_markup=theme_markup.get_history_markup())
        
        if state == 'order_history':
            if call.data == 'repeat_last_order':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=theme_markup.get_repeat_last_order_markup())
            if call.data == 'repeat_specific_order':
                state = 'checking_specific_orders'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=theme_markup.get_repeat_last_order_markup())


# custom cake 
        if call.data == 'custom_cake_about':
            state = 'custom_cake'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, custom_cake_menu_message, reply_markup=theme_markup.get_custom_cake_about_markup())
        
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
                state = 'confirming_custom_order'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=prepare_custom_order_message, reply_markup=theme_markup.get_confirm_custom_order_markup())

        if state == 'confirming_custom_order':
            if call.data == 'confirm_custom_order':
                state = 'entering_delivery_address'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')
# order
        if state == 'confirming_address':
            if call.data == 'reenter_address':
                state = 'entering_delivery_address'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')
            if call.data == 'confirm_address':

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Thank you for your order !')
        
        if state == ''
        

bot.polling()