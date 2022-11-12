
# Mногоязычность

Запускаем первый раз
1. Вытаскиваем тексты из файлов
```shell
pybabel extract . -o locales/password_save_telegram_bot.pot
```
2. Создаем папку для перевода на английский
```shell
pybabel init -i locales/password_save_telegram_bot.pot -d locales -D password_save_telegram_bot -l en
```
3. Переводим, а потом собираем переводы
```shell
pybabel compile -d locales -D password_save_telegram_bot
```


Обновляем переводы
1. Вытаскиваем тексты из файлов, Добавляем текст в переведенные версии
```shell
pybabel extract . -o locales/password_save_telegram_bot.pot
```
```shell
pybabel update -d locales -D password_save_telegram_bot -i locales/password_save_telegram_bot.pot
```
3. Вручную делаем переводы, а потом Собираем
```shell
pybabel compile -d locales -D password_save_telegram_bot
```