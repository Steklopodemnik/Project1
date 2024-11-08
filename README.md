# Telegram Bot для вычисления средних значений

Этот Telegram-бот вычисляет различные средние значения (арифметическое, квадратическое и гармоническое) на основе чисел, введенных пользователем. Пользователь выбирает тип среднего значения с помощью кнопок и вводит числа через пробел. Бот обрабатывает числа и возвращает результат.

## Возможности

- **Выбор типа среднего значения**: арифметическое, квадратическое или гармоническое.
- **Интерактивные кнопки**: с помощью кнопок пользователь может выбирать команды `/1`, `/2`, `/3` и кнопку «Сброс» для сброса настроек.
- **Кнопка «Старт»**: позволяет пользователю начать чат заново с чистого листа.

## Установка

### 1. Установка Python и необходимых библиотек

1. Убедитесь, что у вас установлен Python 3.6+.
2. Установите библиотеку `python-telegram-bot`, выполнив в командной строке:
    ```bash
    pip install python-telegram-bot
    ```

### 2. Создание бота в Telegram

1. Откройте Telegram и найдите [BotFather](https://t.me/botfather).
2. Отправьте команду `/newbot` и следуйте инструкциям, чтобы создать нового бота.
3. Скопируйте полученный токен API для своего бота.

### 3. Настройка кода

1. Скачайте или скопируйте файл `bot.py` в локальную папку.
2. Откройте `bot.py` в текстовом редакторе.
3. Вставьте свой токен API в строку:
    ```python
    token = 'ВАШ_ТОКЕН'
    ```
4. Сохраните файл.

## Запуск

В командной строке перейдите в папку с `bot.py` и запустите команду:

```bash
python bot.py
```

После этого бот начнет работу, и в командной строке отобразится сообщение `Бот запущен...`.

## Использование

1. Найдите вашего бота в Telegram (по имени, которое вы задали при создании) и нажмите «Старт» или введите команду `/start`.
2. Бот предложит выбрать один из типов среднего значения:
   - **1** - Среднее арифметическое
   - **2** - Среднее квадратическое
   - **3** - Среднее гармоническое
3. После выбора типа среднего введите числа через пробел для расчета.
4. Бот вычислит и отправит результат.

### Кнопки

- **1**, **2**, **3** — выбор типа среднего значения.
- **Сброс** — сбрасывает настройки и очищает данные.
- **Старт** — перезапускает взаимодействие с ботом, отображая начальное сообщение.

## Пример использования

1. Нажмите кнопку «1» для выбора среднего арифметического.
2. Введите числа, например, `4 8 15 16 23 42`.
3. Бот отправит результат среднего арифметического этих чисел.

## Описание кода

- **`start`**: отправляет приветственное сообщение и отображает кнопки для взаимодействия.
- **`choose_arith`**, **`choose_quad`**, **`choose_harm`**: обрабатывают выбор пользователя, указывая тип среднего значения, которое он хочет вычислить.
- **`calculate_mean`**: принимает введенные числа, рассчитывает выбранное среднее значение и отправляет результат.
- **`clear_chat`**: сбрасывает настройки и очищает введенные данные, предлагая начать заново.

## Примечания

- Для гармонического среднего введенные числа не должны содержать ноль, иначе бот сообщит об ошибке.
- При ошибочном вводе бот сообщит пользователю, чтобы он ввел числа заново.
