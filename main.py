import tweepy
import json
from keys import Bearer_token as token


# Личный токен, можно просто вставить строкой
BEARER_TOKEN = token

# Инициализация клиента Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_user_info(username, mode):
    try:
        # Используем эндпоинт GET /2/users/by/username/{username}
        response = client.get_user(username=username, user_fields=["name", "description", "public_metrics"])

        # Проверяем, что запрос успешен
        if response.data:
            user = response.data
            user_data = {
                "name": user.name,
                "username": user.username,
                "description": user.description,
                "followers_count": user.public_metrics["followers_count"],
                "tweet_count": user.public_metrics["tweet_count"]
            }
            if mode == "write":
                filename = username + ".json"
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(user_data, file, ensure_ascii=False, indent=4)
            else:
                if mode != "show":
                    print("Неизвестный режим, выбран режим по умолчанию")
                print(user_data)
        else:
            print("Пользователь не найден.")
    except tweepy.errors.TweepyException:
        print("Закончились доступные обращения, подождите пока количество обращений не восстановится")
    except Exception:
        print("Неизвестная ошибка, попробуйте проверить подключение к сети")



while True:    # Менюшка
    print("МЕНЮ:\nИнформация - i\nИскать пользователя - s\nВыход - q")
    respond = str(input())
    if respond == "q":
        break
    elif respond == "s":
        print("Введите имя пользователя:")
        username = input()
        print("Выберите режим (write/show)")
        mode = input()
        get_user_info(username, mode)
    elif respond == "i":
        print("Краткая информация: Эта программа использует API v2 сайта x.com, что позволяет совершать 3 запроса каждые 15 минут\nЕсли такой пользователь существует, в ответ будут получены:\n1)Имя\n2)Никнейм\n3)Краткое описание\n4)Количество подписчиков\n5)Количество твитов")
    else:
        print("Неверный вариант")
        continue
