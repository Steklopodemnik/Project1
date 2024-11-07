from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import math

def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

def quadratic_mean(numbers):
    return math.sqrt(sum(x ** 2 for x in numbers) / len(numbers))

def harmonic_mean(numbers):
    return len(numbers) / sum(1 / x for x in numbers)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["1", "2", "3"],  
        ["Сброс", "Старт"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привет! Я бот для расчета среднего значения.\n"
        "Нажмите одну из кнопок ниже для выбора типа среднего:\n"
        "1 - Среднее арифметическое\n"
        "2 - Среднее квадратическое\n"
        "3 - Среднее гармоническое\n"
        "Или нажмите 'Сброс' для отмены.",
        reply_markup=reply_markup
    )

async def choose_arith(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['choice'] = 'arith'
    await update.message.reply_text("Введите числа через пробел для расчета среднего арифметического.")

async def choose_quad(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['choice'] = 'quad'
    await update.message.reply_text("Введите числа через пробел для расчета среднего квадратического.")

async def choose_harm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['choice'] = 'harm'
    await update.message.reply_text("Введите числа через пробел для расчета среднего гармонического.")

async def calculate_mean(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'choice' not in context.user_data:
        await update.message.reply_text("Сначала выберите тип среднего значения с помощью кнопок '1', '2' или '3'.")
        return

    try:
        numbers = list(map(float, update.message.text.split()))
        if not numbers:
            raise ValueError("Список чисел пуст.")

        choice = context.user_data['choice']
        if choice == 'arith':
            result = arithmetic_mean(numbers)
            await update.message.reply_text(f"Среднее арифметическое: {result}")
        elif choice == 'quad':
            result = quadratic_mean(numbers)
            await update.message.reply_text(f"Среднее квадратическое: {result}")
        elif choice == 'harm':
            if 0 in numbers:
                await update.message.reply_text("Для гармонического среднего числа должны быть ненулевыми.")
            else:
                result = harmonic_mean(numbers)
                await update.message.reply_text(f"Среднее гармоническое: {result}")
    except ValueError:
        await update.message.reply_text("Ошибка ввода. Введите корректные числа через пробел.")

async def clear_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()
    await update.message.reply_text("Все настройки сброшены. Нажмите 'Старт', чтобы начать заново.")

def main():
    token = 'ВАШ ТОКЕН'
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("^1$"), choose_arith))  
    app.add_handler(MessageHandler(filters.Regex("^2$"), choose_quad))   
    app.add_handler(MessageHandler(filters.Regex("^3$"), choose_harm))   
    app.add_handler(MessageHandler(filters.Regex("Сброс"), clear_chat))
    app.add_handler(MessageHandler(filters.Regex("Старт"), start)) 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_mean))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
