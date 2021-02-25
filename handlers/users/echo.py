from aiogram import types

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    # Получаем chat_id и text

    chat_id = message.from_user.id
    text = message.text

    # Необходимо получить объект бота

    # 1 вариант - из диспатчера
    # bot = dp.bot

    # 2 вариант - из контекста
    # from aiogram import Bot
    # bot = Bot.get_current()

    # 3 вариант - из модуля loader
    from loader import bot

    # Отправим сообщение пользователю
    # 1 вариант
    await bot.send_message(chat_id=chat_id, text=text)

    # 2 вариант - без ввода chat_id
    # message.answer(text=text)

    # 3 вариант - с реплаем
    # message.reply()
