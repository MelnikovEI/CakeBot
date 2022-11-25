import telebot
import os

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


@bot.message_handler(commands=['start'])
def button(message):
    with open('BakeCake.pdf', 'rb') as terms_of_service:
        bot.send_document(
                message.chat.id,
                document=terms_of_service,
                caption='You must accept the terms and conditions',
                reply_markup=theme_markup.get_start_markup()
            )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'back_to_main':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            with open(os.path.join('images', 'cake_main.png'), 'rb') as cake_picture:
                bot.send_photo(call.message.chat.id, cake_picture, caption=main_menu_message, reply_markup=theme_markup.get_main_markup())
        if call.data == 'see_cake_menu':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, cake_menu_message, reply_markup=theme_markup.get_cake_menu_markup())
        if call.data == 'see_offers':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, offers_menu_message, reply_markup=theme_markup.get_offers_markup())
        if call.data == 'custom_cake_about':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, custom_cake_menu_message, reply_markup=theme_markup.get_custom_cake_about_markup())
        if call.data == 'last_order_delivery_status':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, last_order_delivery_status_message, reply_markup=theme_markup.get_last_order_delivery_status_markup())
        if call.data == 'see_history':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            bot.send_message(call.message.chat.id, order_history_message, reply_markup=theme_markup.get_history_markup())
        if call.data == 'custom_cake_start':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=custom_cake_levels_message, reply_markup=theme_markup.get_custom_cake_levels_markup())
        if call.data == 'custom_cake_level_1':
            bot.edit_message_text(call.message.chat.id, call.message.id, text=custom_cake_shape_message, reply_markup=theme_markup.get_custom_cake_shape_markup())
        if call.data == 'custom_cake_level_2':
            bot.edit_message_text(call.message.chat.id, call.message.id, text=custom_cake_shape_message, reply_markup=theme_markup.get_custom_cake_shape_markup())
        if call.data == 'custom_cake_level_3':
            bot.edit_message_text(call.message.chat.id, call.message.id, text=custom_cake_shape_message, reply_markup=theme_markup.get_custom_cake_shape_markup())
        
        
        
        
        

        

bot.polling()
