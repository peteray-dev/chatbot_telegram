from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# configure logging

logging.basicConfig(level=logging.INFO)

# initialize the Bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message:types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("Hi\n I am Echo Bot! \n powered by aiogram")


@dp.message_handler()
async def command_start_handler(message:types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



