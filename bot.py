import logging
from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
import string

API_TOKEN = '5568482311:AAH4-tiykq0JmLx1hcW2Vne_wLJmUz0Kit8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nMen \"Uz Imlo Bot\" man.\nMenga so'z yuboring.")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.reply("So'zingizni imlo xatosini tekshirib qaytaraman.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    wordis = message.text
    wordis = wordis.translate(str.maketrans('', '', string.punctuation)).split()
    for word in wordis:
        result = checkWord(word)
        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)