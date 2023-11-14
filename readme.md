# Web-приложение для определения заполненных форм.

Стек используемых технологий:
* FastAPI
* Docker
* Docker-compose
* Mongodb

Описание.
В базе данных хранится список шаблонов форм. 
Шаблон формы - это структура, которая задается уникальным набором полей с указанием их типов.

Так же все поля поддерживают валидацию. 
Принцип работы такой, что на вход по URL /get_form POST запросом передаются данные такого вида:
f_name1=value1&f_name2=value2


В ответ возвращается список имен шаблонов форм, если они были найдены.
Подходящим шаблоном считается тот, поля которого совпали с полями в присланной форме и у которых совпали имя и тип значения. Полей в пришедшей форме может быть больше чем в шаблоне, в этом случае шаблон все равно будет считаться подходящим.

Если подходящей формы не нашлось, вернуть ответ в следующем формате
```json
{
    "f_name1": "FIELD_TYPE",
    "f_name2": "FIELD_TYPE"
}

```
где FIELD_TYPE это тип поля, выбранный на основе правил валидации.
Пример шаблона формы:

```json
{
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
}
```

Всего поддерживаться четыре типа данных полей: 
* email
* телефон
* дата
* текст

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате:
```python
+7 xxx xxx xx xx
```
дата передается в форматах:
```python
YYYY-MM-DD

DD.MM.YYYY
```

В качестве базы данных используется Docker образ с MongoDB.

Инструкция по установке:

Скачайте данный репозиторий

```python
`git clone https://github.com/shmicer/training_system_test_case.git`
```

и выполните команду:

```python
docker-compose -f local.yml up -d --build
```
При сборке контейнера данные шаблонов импортируются в базу данных

Так же в репозитории присутствуют тесты, которые можно запустить командой
```python
docker-compose exec app python main.py pytest
```



