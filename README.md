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
docker run -d --name compnet_nginx --network comp-net-5 -v ./nginx_6.conf:/etc/nginx/conf.d/default.conf:ro -p 80:80 nginx:latest
```

## Использование
- http://127.0.0.1/parse
- http://127.0.0.1/get-data


# Задание 7
Прикрутить заглушку по Российскому IP / prefix. То есть переходя с РФ ip должен сработать РЕДИРЕКТ на любую заглушку вроде "ВАМ СЮДА НЕЛЬЗЯ". Важно! заглушка должна быть реализована на уровне сервера, а не вашего приложения.

## Подготовка

### Вся подготовка 5-го задания + добавили файл nginx_7.conf
### Создать образ nginx, и запустить его контейнер
```bash
docker pull nginx
```
```bash
docker run -d --name compnet_nginx --network comp-net-5 -v ./nginx_7.conf:/etc/nginx/conf.d/default.conf:ro -p 80:80 -p 8081:8081 nginx:latest
```

## Использование
- http://127.0.0.1/parse
- http://127.0.0.1/get-data