from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboards.key_inline import get_keyboard_inline, get_back_to_keyboard
from texnic.texnic import texnic

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f'Привет, {user_name}, в этом боте ты можешь узнать о основной технике армии России: ', reply_markup= get_keyboard_inline())

@dp.callback_query_handler(lambda c: c.data.startswith('texnic_'))
async def process_rank(callback_query: types.CallbackQuery):
    texnic_name = callback_query.data.split('_')[1]
    texnic_info = texnic.get(texnic_name)

    if texnic_info:
        await bot.send_photo(callback_query.message.chat.id, photo=texnic_info["image_url"], caption=texnic_info["description"], reply_markup=get_back_to_keyboard())
    else:
        await bot.send_message(callback_query.message.chat.id, "Техника не найдена")

@dp.callback_query_handler(lambda c: c.data == "back_to_list")
async def back_to_list(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Выберите технику:", reply_markup=get_keyboard_inline())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)