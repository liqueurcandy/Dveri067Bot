from telegram import Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes # type: ignore
from telegram import InlineKeyboardButton, InlineKeyboardMarkup # type: ignore

# Replace 'YOUR_BOT_TOKEN' with the token from @BotFather
BOT_TOKEN = '7907503930:AAHrfx5V_88OcUrylFnhBR4PJzIi0ifUF2c'

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚪 Добро пожаловать в @Dveri067Bot! Ваш помощник по дверям, окнам и фурнитуре от Dveri067.ru в Смоленске! 🏠\n"
        "📋 Что я умею:\n"
        "/catalog - Посмотреть двери, окна и фурнитуру\n"
        "/quote - Запросить стоимость\n"
        "/consult - Записаться на консультацию\n"
        "/help - Получить помощь"
    )


async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Входные двери", callback_data="entry_doors")],
        [InlineKeyboardButton("Межкомнатные двери", callback_data="interior_doors")],
        [InlineKeyboardButton("Окна", callback_data="windows")],
        [InlineKeyboardButton("Фурнитура", callback_data="fittings")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🛠️ Выберите категорию:", reply_markup=reply_markup)
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Чтобы получить стоимость, напишите, что вам нужно (например, 'входная дверь, 90x200 см') или используйте /consult для детальной консультации!"
    )

async def consult(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Запишитесь на консультацию! Напишите ваш телефон или свяжитесь с нами: info@dveri067.ru или +7 (XXX) XXX-XX-XX."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ Нужна помощь? Я @Dveri067Bot! Используйте:\n"
        "/start - Начать\n"
        "/catalog - Каталог товаров\n"
        "/quote - Узнать цены\n"
        "/consult - Записаться на консультацию\n"
        "Вопросы? Пишите: info@dveri067.ru"
    )

def main():
    # Initialize the bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("catalog", catalog))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("consult", consult))
    app.add_handler(CommandHandler("help", help))

    # Start the bot
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()