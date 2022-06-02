import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    message = str(settings.tg_message)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': message
    })

    if message.find('{') and message.find('}') and message.rfind('{') and message.rfind('}'):

        part_1 = message[0:message.find('{')]
        part_2 = message[message.find('}') + 1:message.rfind('{')]
        part_3 = message[message.rfind('}'):-1]

        text_slise = part_1 + tg_name + part_2 + tg_phone + part_3

    try:
        req = requests.post(method, data={
            'chat_id': chat_id,
            'text': text_slise
        })
    except:
        pass
    finally:
        if req.status_code != 200:
            print('Ошибка отправки!')
        elif req.status_code == 500:
            print('Ошибка 500')
        else:
            print('Все ОК сообщение отправленно!')
    pass



