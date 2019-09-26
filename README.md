# Raspberry Pi Telegram Bot

## Telegram бот на Raspberry Pi в Docker контейнере
```
на основе [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
```

```
По запросу показывает температуру с присоедиенного датчика DTH22
```

### Технологии
 - Docker, docker-compose
 - Python

### Установка и запуск
 - Регистрируем своего бота [здесь](https://core.telegram.org/bots#3-how-do-i-create-a-bot), запоминаем/копируем его токен и @имя.
 - Ставим docker и docker-compose (ищем в инете как)
 - Клонируем репозиторий в `/srv/tbot` - все конфиги заточены под эту директорию
 - Редактируем [Dockerfile](https://github.com/vsb2007/raspberry_telegram_bot2/blob/master/Dockerfile) - можно все оптимизировать, чтобы было меньше слоев, 
я оставил так, чтобы было понятнее, что происходит.
 - Собираем свой образ `sh docker_build.sh`, преварительно поменяв в `docker-compose.yml` [vsb2007](https://github.com/vsb2007/raspberry_telegram_bot2/blob/eb46c118f6f6fa0cabf7323a7100e22bac73e74f/docker-compose.yml#L5) 
и в `docker_build.sh` [vsb2007](https://github.com/vsb2007/raspberry_telegram_bot2/blob/497bf655755e04479f1314706a1186c5d64d22d5/docker_build.sh#L3) на что-то свое
 - Открываем фаил [myconfig.py.sample](config/myconfig.py.sample), убираем расширение `.sample` и подставляем свои данные
 - запускаем бота `docker-compose up -d`
 - Добавляем бота в группу или общаемся напрямую с ним. В данном примере команда `/temp` вернет
```
temp:  21.8
humidity: 25.5
```
или что-то похожее :-)
