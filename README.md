Долгов Даниил, ИИР, 24944

# Задание 5
Развернуть отдельно 2 докер контейнера, (БЕЗ  docker-compose) и настроить сеть между ними. 1-й контейнер - ваше приложение (на порту отличном от 80), 2-й контейнер - база данных

## Подготовка

### Выполнять команды в папке задания
### Создать сеть
```bash
docker network create comp-net-5
```

### Создать образы
```bash
docker pull postgres
```
```bash
docker build -t compnet/app .
```

### Запустить контейнеры
```bash
docker run -d --name compnet_db --network comp-net-5 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgregory1 -e POSTGRES_DB=DB_4 postgres
```
```bash
docker run -d --name compnet_app --network comp-net-5 -p 8080:8080 compnet/app
```

## Использование
- http://127.0.0.1:8080/parse
- http://127.0.0.1:8080/get-data


# Задание 6
Настроить проксирование, таким образом, чтобы запросы на 80 порт перенаправлялись в ваше приложение в докер контейнере

## Подготовка

### Вся подготовка 5-го задания + добавили файл nginx_6.conf
### Создать образ nginx, и запустить его контейнер
```bash
docker pull nginx
```
```bash
docker run -d --name compnet_nginx_6 --network comp-net-5 -v ./nginx_6.conf:/etc/nginx/conf.d/default.conf:ro -p 80:80 nginx:latest
```

## Использование
- http://127.0.0.1/parse
- http://127.0.0.1/get-data


# Задание 7
Прикрутить заглушку по Российскому IP / prefix. То есть переходя с РФ ip должен сработать РЕДИРЕКТ на любую заглушку вроде "ВАМ СЮДА НЕЛЬЗЯ". Важно! заглушка должна быть реализована на уровне сервера, а не вашего приложения. Российские адреса: https://scanitex.com/en/resources/ip-ranges/ru

## Подготовка

### Вся подготовка 5-го задания + добавили файл nginx_7.conf
### Создать образ nginx, и запустить его контейнер (остановить контейнер из задания 6)
```bash
docker pull nginx
```
```bash
docker run -d --name compnet_nginx_7 --network comp-net-5 -v ./nginx_7.conf:/etc/nginx/conf.d/default.conf:ro -v ./ru.conf:/etc/nginx/ru.conf:ro -p 80:80 -p 7777:7777 nginx:latest
```

## Использование
- http://2.59.160.0/parse
- http://5.10.0.0/parse


# Задание 8
Сделать так, чтобы ваше приложение было доступно на моём пк, то есть вы присылаете мне ip, и у меня открывается ваш проект. Метод реализации этого ничем не ограничен.

## Подготовка
### Всё то же самое, что и в 7-м задании
### Создать туннель от моего приложения на сервер в интернете
```bash
ssh -R 80:localhost:80 ssh.localhost.run
```

## Использование
- Ссылка, которую я получу при туннелировании


# Задание 10
Сначала руками в терминале, а затем скриптом на любом ЯП:
Выполнить DNS-запросы для списка доменов.
Сохранить их IP-адреса.
Выполнить traceroute для каждого IP-адреса.
Сохранить результаты в CSV-файл.

## Использование (в папке задания)
```bash
python traceroute.py
```