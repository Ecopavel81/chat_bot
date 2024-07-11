from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.random_fox import fox
from less3.keybords.keyboards import kb1, kb2
from random import randint


router = Router()


#Хендлер на команду /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет! {name} Я эхобот на aiogram 3.'\
                        'Отправь мне любое сообщение, и я повторю его,', reply_markup = kb1)


#Хендлер на команду /info
@router.message(Command("info"))
async def info(message: types.Message):
    await message.answer("Я новый бот")


#Хендлер на команду /user
@router.message(Command("user"))
async def echo(message: types.Message):
    await message.answer(f'Привет, polzavatel')

#Хендлер на команду /stop
@router.message(Command("stop"))
async def stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}')


#Хендлер на команду /fox
@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo = img_fox)
    #await bot.send_photo(message.from_user.id, photo = img_fox)


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')


#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji='🎲')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup = kb2)
    elif '/prof' in msg_user:
        await message.answer_dice(emoji='🎲')
    else:
        await message.answer(f'Я не знаю такого слова')


#1 usage
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())