from telegram import (
    Update, InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, InputFile
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

TOKEN = "8346277331:AAEuTBp9kShxULJf2RfQmtWCw7h8MPGe7sk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [["🧃🍫товары", "😡 жалоба"], ["🧑‍💼 вакансия", "❓ помощь"], ["🤝сотрудничать"], ["если мы в telegram?"], ["👌🎫ввести проммокод", "wfa", "takis", "azbuisness"], ["📞контакты"], ["🍫🧃🍬полное меню товаров"]]
    await update.message.reply_text(
        f"Привет, {update.effective_user.first_name}!",
        reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True)
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команды:\n/start — братское меню👌\n/help — помощь\n/buttons — пример кнопок"
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[
        InlineKeyboardButton("🌐 Telegram", url="https://telegram.org"),
        InlineKeyboardButton("📂 Файл", callback_data="file")
    ]]
    await update.message.reply_text("Инлайн-кнопки:", reply_markup=InlineKeyboardMarkup(kb))

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "file":
        await query.message.reply_document(InputFile("example.txt"))

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text.lower()
    if "🧃🍫товары" in t:
        await update.message.reply_text("Karl Gummies🍬 - 36AZN; Takis Big🔥 - 30AZN; PRIME🧃 - 17AZN; ЧТОБ ПОСМОТРЕТЬ ДРУГИЕ ТОВАРЫ ПЕРЕХОДИТЕ ПО ЭТОЙ ССЫЛКЕ: https://wa.me/c/994776236100")
    elif "😡 жалоба" in t:
        await update.message.reply_text("Если хотите написать жалобу то в таком случае пишите на этот номер и вы свяжетесь с нашим Администратором : +994 998 44 04 03")
    elif "🧑‍💼 вакансия" in t:
        await update.message.reply_text("Если хотите работать с нами то пожалуйста пишите на этот номер : +994 50 334 24 06")
    elif "помощь" in t:
        await update.message.reply_text("Какие то проблемы? Обращяйся к нашему модератору : +994 50 334 24 06")
    elif "🤝сотрудничать" in t:
        await update.message.reply_text("Хотите заработать бабла💸 с вашего бизнеса? то вы можете сотрудничать с нами🧑‍💼🤝🧑‍💼 пишите на этот номер : +994 77 623 61 00")
    elif "если мы в telegram?" in t:
        await update.message.reply_text("К сожелению мы не в Telegram но скоро все будет!")
    elif "👌🎫ввести проммокод" in t:
        await update.message.reply_text("Выберите промокод который хотите использовать - WFA; TAKIS; AZBUISNESS - СРОЧНО ВВЕДИТЕ ИХ ВЕДЬ С 10 НОЯБРЯ ОНИ ПРОПАДУТ😢")
    elif "wfa" in t:
        await update.message.reply_text("ПОЗДРОВЛЯЮ ВЫ ПОЛУЧИЛИ СКИДКУ🔥 НА PRIME🧃, FEASTABLES🍫, И LIT ENERGY⚡; ЧТОБ ПОЛУЧИТЬ ЭТО ВСЕ СО СКИДКОЙ СНИМИТЕ ЭТО И ПРИШЛИТЕ НА ЭТОТ НОМЕР : +994 993 21 07 75")
    elif "takis" in t:
        await update.message.reply_text("ПОЗДРОВЛЯЮ ВЫ ПОЛУЧИЛИ СКИДКУ🔥 НА БОЛЬШОЙ ТАКИС ТЕПЕРЬ ТОЛЬКО ДЛЯ ВАС ОН СТОИТ 25AZN; ЧТОБ ПОЛУЧИТЬ ЭТО ВСЕ СО СКИДКОЙ СНИМИТЕ ЭТО И ПРИШЛИТЕ НА ЭТОТ НОМЕР : +994 993 21 07 75")
    elif "azbuisness" in t:
        await update.message.reply_text("ПОЗДРОВЛЯЮ ВЫ ПОЛУЧИЛИ СКИДКУ 10% НА ВСЕ ТОВАРЫ ДО 4 НОЯБРЯ🔥  ; ЧТОБ ПОЛУЧИТЬ ЭТО ВСЕ СО СКИДКОЙ СНИМИТЕ ЭТО И ПРИШЛИТЕ НА ЭТОТ НОМЕР : +994 993 21 07 75")
    elif "📞контакты" in t:
        await update.message.reply_text("Хотите посмотреть контакты еще раз? Пожалуйста!: 🧑‍💼Владенец Компании - +994 77 623 61 00; 👨‍💻Администратор - +994 998 44 04 03; 👨‍💻Модератор - +994 50 334 24 06; 👨‍💻🎫Для промокодов - +994 993 21 07 75 ")
    elif "🍫🧃🍬полное меню товаров" in t:
        await update.message.reply_text("Не работает ссылка? Все ок щас я вам отправлю все меню - 🔥Takis s - 4AZN💵; 🔥🔥Takis m - 10AZN💵; 🔥🔥🔥Takis b - 30AZN💵; 🍬Karl Gummies - 36AZN💵; 🧃Prime -17AZN💵; ⚡Monster - 7AZN💵; 🍫FEASTABELS - 16AZN💵; 🧃Dr.Pepper - 5AZN💵; 🍬Sour Patch Kids s - 2AZN💵; 🍬Sour Patch Kids m - Еще не на продаже; 🍬Sour Patch Kids B - 5.70AZN💵; 🧃НАШ СОБСТВЕНЫЙ ПРОДУКТ - СКОРО НА ПРОДАЖЕ!; 🧃⚡LIT ENERGY - 11AZN💵; 😖🍋JAPANESE SOURE SNACK - 15AZN💵; 😖🍋TOXIC WASTE - 15AZN💵; 🍬CHUPA CHUPS GUM - 20AZN💵; 🧃⚡PRIME ENERGY - 20AZN💵: СКОРО ТУТ ВСЕ БУДЕТ НО НА ВСЯКИЙ ДЕРЖИТЕ ССЫЛКУ : https://wa.me/c/994776236100")

    else:
        await update.message.reply_text(f"Ты сказал: {update.message.text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("buttons", buttons))
app.add_handler(CallbackQueryHandler(callback))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text))

print("🤖 Бот запущен...")
app.run_polling()