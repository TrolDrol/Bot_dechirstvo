import datetime
import time
import telebot
import requests
from tokens_tel_bots import token_bot_dechirstvo, chat_id_class_group

token = token_bot_dechirstvo
bot = telebot.TeleBot(token)
chat_id = chat_id_class_group

time_five_minyt = 300

f = open('cache_bot_dechirstvo.txt')
count_parta, count_riad = map(int, f.readline().split())
f.close()

parta = ['1','2','3','4']
riad = ['1','2','3']

time_str = input('Введите время в формате ЧЧ:ММ:СС : ')
later = int(input('Введите примерное время ожидания в минутах: '))

time.sleep(later * 60)

while True:
    now_time = datetime.datetime.now()
    day_of_the_week = str(datetime.datetime.date(now_time).isoweekday())
    now_time_time = datetime.datetime.strftime(now_time,'%H:%M:%S')
    if now_time_time == time_str and day_of_the_week in ('1','2','3','4','5','6'):
        if count_parta > 3:
            count_parta = 0
        if count_riad > 2:
            count_riad = 0
        parta_today = parta[count_parta]
        riad_today = riad[count_riad]
        count_parta += 1
        count_riad += 1
        f = open('cache_bot_dechirstvo.txt', 'r+')
        f.write(f'{count_parta} {count_riad}')
        f.close()
        message = f'Сегодня дежурит {parta_today} парта на {riad_today} ряду.'
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        try:
            print(requests.get(url).json())
            time.sleep(86_300)
        except requests.exceptions.ConnectionError:
            print('Ошибка')
            time.sleep(time_five_minyt)
            print(requests.get(url).json())
            time.sleep(86_300)
    elif day_of_the_week == '7':
        time.sleep(86_300)
    else:
        pass
