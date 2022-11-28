import os

import telebot
from telebot import types

import db_api
import theme_markup
from bake_cake import setup

bot = telebot.TeleBot('5930122900:AAG0d2Wxllm1Z5cb6E3AFDXBxM3czITkBzc')

main_menu_message = 'Hello! You are in main menu'
cake_menu_message = 'Here you can choose your favourite cake'
offers_menu_message = 'See our special offers today'
custom_cake_menu_message = 'More options for making your dream cake'
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

def approximate_delivery_time(order):
    test = 'test'
    return test
    


def get_cake_name_by_id(needed_id, list):
    for list_item in list:
        if list_item.get("id") == needed_id:
            name = list_item.get("title")
            return name


def generate_markup_for_multiple_choice_cakes(list):
    markups = []
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    max_choices = 5
    split_lists = get_split_list(list, max_choices)
    for split_list in split_lists:
        markup = types.InlineKeyboardMarkup()
        for split_list_item in split_list:
            button = types.InlineKeyboardButton(f'{split_list_item.get("title")} - {split_list_item.get("price")} Rub', callback_data=f'list_position_id_{split_list_item.get("id")}')
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
    
def generate_markup_for_multiple_choice_orders(list):
    markups = []
    back_to_main = types.InlineKeyboardButton('Exit', callback_data='back_to_main')
    max_choices = 5
    split_lists = get_split_list(list, max_choices)
    for split_list in split_lists:
        markup = types.InlineKeyboardMarkup()
        for split_list_item in split_list:
            button = types.InlineKeyboardButton(f'Date: {split_list_item.get("date")}  {split_list_item.get("time")} - {get_cake_name_by_id(split_list_item.get("cake_id"), menu_cakes)}', callback_data=f'list_position_id_{split_list_item.get("id")}')
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

    
cake_levels = db_api.get_levels()
cake_shapes = db_api.get_shapes()
cake_toppings = db_api.get_toppings()
cake_berries = db_api.get_berries()
cake_decorations = db_api.get_decors()

menu_cakes = db_api.get_standard_cakes()

custom_cake_markups = generate_markups_for_custom_cake(cake_levels, cake_shapes, cake_toppings, cake_berries, cake_decorations)
cake_menu_markup = generate_markup_for_multiple_choice_cakes(menu_cakes)
state = 'pending'


@bot.message_handler(commands=['start'])
def enter_main_menu(message):
    global created_order
    global state
    global message_to_delete
    global cake_customisation
    global menu_cake_id
    if db_api.get_pd_status(message.from_user.id):
            state = 'main'
            menu_cake_id = ''
            created_order = {
                'client_id': message.from_user.id,
                'delivery_datetime': '',
                'delivery_address': '',
                'receiver': '',
                'is_urgent': False,
                'comment': '',
                'status': '',
            }
            cake_customisation = {
                'level': '',
                'shape': '',
                'topping': '',
                'berries': '',
                'decor': '',
                'inscription': '',
            }
            with open(os.path.join('images', 'cake_main.png'), 'rb') as cake_picture:
                bot.send_photo(message.chat.id, cake_picture, caption=main_menu_message, reply_markup=theme_markup.get_main_markup())
    else:    
        with open('BakeCake.pdf', 'rb') as terms_of_service:
            bot.send_document(
                    message.chat.id,
                    document=terms_of_service,
                    caption='You must accept the terms and conditions',
                    reply_markup=theme_markup.get_start_markup()
                )

@bot.message_handler(content_types=['text'])
def process_answer(message):
    global created_order
    global state
    global message_to_delete
    global cake_customisation
    global menu_cake_id
    if state == 'adding_inscription':
        state = 'confirming_inscription'
        inscription = message.text
        print(inscription)
        cake_customisation['inscription'] = inscription
        bot.delete_message(message_to_delete.chat.id, message_to_delete.id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The inscription is: {inscription}. Confirm ?', reply_markup=theme_markup.get_inscription_confirm_markup())
    if state == 'entering_delivery_address':
        state = 'confirming_address'
        address = message.text
        print(address)
        created_order['delivery_address'] = address
        bot.delete_message(message_to_delete.chat.id, message_to_delete.id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The address is: {address}. Confirm ?', reply_markup=theme_markup.get_address_confirm_markup())
    if state == 'entering_receiver_name':
        state = 'confirming_receiver'
        receiver = message.text
        print(receiver)
        created_order['receiver'] = receiver
        bot.delete_message(message_to_delete.chat.id, message_to_delete.id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The receiver is: {receiver}. Confirm ?', reply_markup=theme_markup.get_receiver_confirm_markup())
    if state == 'entering_comment':
        state = 'confirming_comment'
        comment = message.text
        print(comment)
        created_order['comment'] = comment
        bot.delete_message(message_to_delete.chat.id, message_to_delete.id)
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, text=f'The comment is: {comment}. Confirm ?', reply_markup=theme_markup.get_comment_confirm_markup())
            

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global created_order
    global state
    global message_to_delete
    global cake_customisation
    global menu_cake_id
    if call.message:
        if call.data == 'back_to_main' or 'accept_conditions':
            if call.data == 'accept_conditions':
                db_api.add_client(call.message.from_user.id, pd_read=True)
            state = 'main'
            menu_cake_id = ''
            created_order = {
                'client_id': call.message.from_user.id,
                'delivery_datetime': '',
                'delivery_address': '',
                'receiver': '',
                'is_urgent': False,
                'comment': '',
                'status': '',
            }
            cake_customisation = {
                'level': '',
                'shape': '',
                'topping': '',
                'berries': '',
                'decor': '',
                'inscription': '',
            }
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
                menu_cake_id = (int(call.data.split("_")[3]))
                print('Chosen cake id: ' + menu_cake_id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'You have selected {get_cake_name_by_id(int(call.data.split("_")[3]), menu_cakes)}', reply_markup=theme_markup.get_menu_cake_confirm_markup())
            if 'decline_order_menu_cake' in call.data:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=cake_menu_message, reply_markup=cake_menu_markup[0])
            if 'confirm_order_menu_cake' in call.data:
                print(menu_cake_id)
                state = 'entering_delivery_address'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')

                
# delivery status
        if call.data == 'last_order_delivery_status':
            state = 'last_order_status'
            orders = db_api.get_orders(call.message.from_user.id)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            if len(orders) > 0:
                last_order = orders[-1]
                if last_order.get('status') == 'completed':
                    bot.send_message(call.message.chat.id, 'Your last order is completed', reply_markup=theme_markup.get_last_order_delivery_status_markup())
                if last_order.get('status') == 'delivery': 
                    bot.send_message(call.message.chat.id, f'Your order was made on {last_order.get("date")} {last_order.get("date")}, and it will approximately arrive at {approximate_delivery_time(last_order)}', reply_markup=theme_markup.get_last_order_delivery_status_markup())
                if last_order.get('status') == 'pending':
                    bot.send_message(call.message.chat.id, 'Your last order is waiting to be processed', reply_markup=theme_markup.get_last_order_delivery_status_markup())
                if last_order.get('status') == 'cancelled':
                    bot.send_message(call.message.chat.id, 'Your last order is canceled', reply_markup=theme_markup.get_last_order_delivery_status_markup())
                if last_order.get('status') == 'accepted':
                    bot.send_message(call.message.chat.id, 'Your last order is being processed', reply_markup=theme_markup.get_last_order_delivery_status_markup())
            else: 
                bot.send_message(call.message.chat.id, 'You dont have any orders', reply_markup=theme_markup.get_last_order_delivery_status_markup())
                
# history 
        if call.data == 'see_history':
            state = 'order_history'
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, 'Check your order history', reply_markup=theme_markup.get_history_markup())
        if state == 'order_history':
            orders = db_api.get_orders(call.message.from_user.id)
            if call.data == 'repeat_last_order':
                if len(orders) > 0:
                    last_order = orders[-1]
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='This is your last order: ', reply_markup=theme_markup.get_repeat_last_order_markup())
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='You dont have any orders', reply_markup=theme_markup.get_last_order_delivery_status_markup())
            if call.data == 'repeat_specific_order':
                if len(orders) > 0:
                    user_history_markup = generate_markup_for_multiple_choice_orders(orders)
                    state = 'checking_specific_orders'
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Your previous orders', reply_markup=user_history_markup[0])
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='You dont have any orders', reply_markup=theme_markup.get_last_order_delivery_status_markup())


        if state == 'checking_specific_orders':
            if 'markup_next_from' in call.data:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Your previous orders', reply_markup=user_history_markup[int(call.data.split('_')[3])+1])
            if 'markup_back_from' in call.data:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Your previous orders', reply_markup=user_history_markup[int(call.data.split('_')[3])-1])
            if 'list_position_id' in call.data:
                print(call.data)


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
                cake_customisation['level'] = int(call.data.split('_')[1])
                state = 'choosing_cake_shapes'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_shape_message, reply_markup=custom_cake_markups[1])

        if state == 'choosing_cake_shapes':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_levels'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_levels_message, reply_markup=custom_cake_markups[0])
            if 'shape' in call.data:
                print(call.data.split('_')[1])
                cake_customisation['shape'] = call.data.split('_')[1]
                state = 'choosing_cake_toppings'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_topping_message, reply_markup=custom_cake_markups[2])

        if state == 'choosing_cake_toppings':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_shapes'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_shape_message, reply_markup=custom_cake_markups[1])
            if 'topping' in call.data:
                print(call.data.split('_')[1])
                cake_customisation['topping'] = call.data.split('_')[1]
                state = 'choosing_cake_berries'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_berries_message, reply_markup=custom_cake_markups[3])

        if state == 'choosing_cake_berries':
            if call.data == 'back_to_previous_state':
                state = 'choosing_cake_toppings'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_topping_message, reply_markup=custom_cake_markups[2])
            if 'cake_berry_' in call.data:
                print(call.data.split('_')[2])
                cake_customisation['berries'] = call.data.split('_')[2]
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
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_receive_inscription_message)
            if call.data == 'no_inscription':
                state = 'entering_delivery_address'
                print('no inscription')
                cake_customisation['inscription'] = 'no inscription'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')

        if state == 'confirming_inscription':
            if call.data == 'confirm_iscription':
                state = 'entering_delivery_address'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')
# order
        if state == 'confirming_address':
            if call.data == 'reenter_address':
                state = 'entering_delivery_address'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter your address')
            if call.data == 'confirm_address':
                state = 'entering_receiver_name'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Enter the name of the receiver')

        if state == 'confirming_receiver':
            if call.data == 'confirm_receiver':
                state = 'entering_comment'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter a comment to your order')
            if call.data == 'reenter_receiver':
                state = 'entering_receiver_name'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Enter the name of the receiver')

        if state == 'confirming_comment':
            if call.data == 'confirm_comment':
                state = 'confirming_urgent'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='To receive your order quicker you can pay 500 Rub for a faster delivery', reply_markup=theme_markup.get_urgent_confirm_markup())
            if call.data == 'reenter_comment':
                state = 'entering_comment'
                message_to_delete = call.message
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Please enter a comment to your order')
        if state == 'confirming_urgent':
            if call.data == 'confirm_urgent':
                print('Urgent - True')
                created_order['is_urgent'] = True
                new_order_personal_key = db_api.add_order(created_order['client_id'], db_api.get_current_datetime, db_api.get_estimate_delivery_datetime(db_api.get_current_datetime, created_order['is_urgent']), created_order['delivery_address'], created_order['is_urgent'], created_order['receiver'], created_order['comment'], 'pending')
                if len(menu_cake_id) > 0:
                    db_api.add_cake_to_order(new_order_personal_key, menu_cake_id)
                else:
                    custom_cake_personal_key = db_api.create_cake(cake_customisation['level'],cake_customisation['shape'], cake_customisation['topping'], cake_customisation['berries'], cake_customisation['decor'], cake_customisation['inscription'])
                    db_api.add_cake_to_order(new_order_personal_key, custom_cake_personal_key)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Thank you for your order. You can check its status in the main menu', reply_markup=theme_markup.get_order_finish_markup())
            if call.data == 'not_urgent':
                print('Urgent - False')
                created_order['is_urgent'] = False
                new_order_personal_key = db_api.add_order(created_order['client_id'], db_api.get_current_datetime, db_api.get_estimate_delivery_datetime(db_api.get_current_datetime, created_order['is_urgent']), created_order['delivery_address'], created_order['is_urgent'], created_order['receiver'], created_order['comment'], 'pending')
                if len(menu_cake_id) > 0:
                    db_api.add_cake_to_order(new_order_personal_key, menu_cake_id)
                else:
                    custom_cake_personal_key = db_api.create_cake(cake_customisation['level'],cake_customisation['shape'], cake_customisation['topping'], cake_customisation['berries'], cake_customisation['decor'], cake_customisation['inscription'])
                    db_api.add_cake_to_order(new_order_personal_key, custom_cake_personal_key)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Thank you for your order. You can check its status in the main menu', reply_markup=theme_markup.get_order_finish_markup())



if __name__ == '__main__':
    setup()
    bot.polling()