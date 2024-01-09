﻿import telebot
from telebot import types
import stripe

# Установите ваш секретный ключ Stripe
stripe.api_key = "sk_test_51OWJXRE52bqgjzEYJW3RgrHLvN21Tj0UPFLCOyrd6gWCDVf7rUwmfYapRvwkbuEQye6AtLHcmaG43qprA602npSp0065TLDZme"

token = '6401653716:AAEhwr3_dPCu02na3l62IokaMnKI8JR7acw'
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
item1 = types.KeyboardButton("Что такое ДВИЖ?")
item2 = types.KeyboardButton("❓Когда следующий ДВИЖ?")
item3 = types.KeyboardButton("Какие трэки хотите услышать?")
item4 = types.KeyboardButton("🎫 Билеты")
item5 = types.KeyboardButton("Наш инстаграм")
item6 = types.KeyboardButton("Переход в обычный канал")
item7 = types.KeyboardButton("Назад")

markup.add(item1, item2, item3, item4, item5, item6, item7)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Выберите, что хотите узнать:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == "Наш инстаграм":
        inline_markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton("Перейти по ссылке", url="https://www.instagram.com/na___dvizh?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")
        inline_markup.add(url_button)
        bot.send_message(message.chat.id, "Вы выбрали кнопку 'Наш инстаграм'. Переходите по ссылке:", reply_markup=inline_markup)
    elif message.text == "Что такое ДВИЖ?":
        bot.send_message(message.chat.id, "Мы самая крупная и громкая тусовка, которую вы только можете посетить, у нас играет музыка на любой вкус. Мы начали свою историю в 2023 году и планируем заниматься организацией на протяжении всей вашей жизни")
    elif message.text == "❓Когда следующий ДВИЖ?":
        bot.send_message(message.chat.id, "На данный момент к сожалению точной информации и даты касательно следующего движа - нету. Следите за информацией!")
    elif message.text == "Переход в обычный канал":
        inline_markup = types.InlineKeyboardMarkup()
        channel_button = types.InlineKeyboardButton("Перейти в канал", url="https://t.me/na_dv1zh")
        inline_markup.add(channel_button)
        bot.send_message(message.chat.id, "Переход в обычный канал:", reply_markup=inline_markup)
    elif message.text == "Какие трэки хотите услышать?":
        bot.send_message(message.chat.id, "Введите треки, которые вы хотели бы услышать, через запятую:")
        bot.register_next_step_handler(message, process_tracks_input)
    elif message.text == "🎫 Билеты":
        try:
            handle_payment(message)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка при обработке команды 'Билеты': {e}")
    elif message.text == "Назад":
        try:
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")
    else:
        bot.send_message(message.chat.id, "Вы написали: " + message.text)

def process_tracks_input(message):
    tracks = message.text
    with open('C:\\Users\\admin\\Desktop\\Programm\\Na Dvizh bot\\Na Dvizh bot\\tracks.txt', 'a') as file:
        file.write(tracks + '\n')

    bot.send_message(message.chat.id, "Спасибо за ваши треки, передадим их диджеям!")

def handle_payment(message):
    chat_id = message.chat.id
    message_id = message.message_id

    # Готовая ссылка на продукт из Stripe
    product_checkout_link = "https://buy.stripe.com/test_7sIcQhbET971dz25kk"  # Замените на реальную ссылку

    # Создаем сообщение с ссылкой на оплату
    payment_message = f"Оплатите билет [здесь]({product_checkout_link})"
    
    # Создаем сессию оплаты
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Ticket',
                },
                'unit_amount': 100,  # Цена в центах (1000 центов = $10.00)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'https://example.com/success?chat_id={chat_id}&message_id={message_id}',
        cancel_url='https://example.com/cancel',
    )

    # Сохраняем ID сессии в текстовый файл
    with open('session_id.txt', 'w') as session_file:
        session_file.write(session.id)

    # Отправляем пользователю сообщение с ссылкой на оплату
    bot.send_message(chat_id, payment_message, reply_to_message_id=message_id, parse_mode="Markdown")

if __name__ == "__main__":
    bot.polling(none_stop=True)
    