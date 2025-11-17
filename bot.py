from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["👕 Каталог", "📦 Як замовити", "📏 Розміри", "🇺🇦 Про бренд", "💬 Підтримка"]
    keyboard.add(*buttons)

    await message.answer(
        "Вітаємо в Liberty Style 👋\n"
        "Бренд шкільного одягу 🇺🇦\n\n"
        "Оберіть розділ нижче:",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "👕 Каталог")
async def catalog(message: types.Message):
    await message.answer(
        "👔 Сорочки\n"
        "🧥 Піджаки\n"
        "👖 Штани\n"
        "👗 Сукні\n"
        "🎒 Аксесуари\n\n"
        "Напишіть, що вас цікавить 👇"
    )

@dp.message_handler(lambda message: message.text == "📦 Як замовити")
async def order_info(message: types.Message):
    await message.answer(
        "🛍 Як зробити замовлення:\n"
        "1️⃣ Напишіть товар і розмір\n"
        "2️⃣ Ми підтвердимо наявність\n"
        "3️⃣ Оплата — на картку / WayForPay\n"
        "4️⃣ Відправка — Нова Пошта / Укрпошта"
    )

@dp.message_handler(lambda message: message.text == "📏 Розміри")
async def sizes(message: types.Message):
    await message.answer(
        "📏 Таблиця розмірів:\n\n"
        "128 – 8 років\n"
        "134 – 9 років\n"
        "140 – 10 років\n"
        "146 – 11 років\n"
        "152 – 12 років\n"
        "158 – 13 років\n"
        "164 – 14 років"
    )

@dp.message_handler(lambda message: message.text == "🇺🇦 Про бренд")
async def about(message: types.Message):
    await message.answer(
        "Liberty Style — український бренд шкільного одягу.\n"
        "Створений з турботою, стилем та якістю.\n"
        "Підтримуємо 🇺🇦 економіку та українських учнів."
    )

@dp.message_handler(lambda message: message.text == "💬 Підтримка")
async def support(message: types.Message):
    await message.answer(
        "Написати менеджеру:\n"
        "@LibertyStyleSupport"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
