from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

MODEL_NAME = "gpt-3.5-turbo"

# initialize the Bot
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

class Reference: #store in memory
    def __init__(self):
        self.response =""

reference = Reference()

def clear_past(): #clear memory
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message:types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("Hi\n I am a chatBot! \n created by minded")

@dispatcher.message_handler(commands=['help'])
async def helper(message:types.Message):
    """
    This handler receives messages with `/start` command
    """
    help_command = """
    Hi, I am a chatbot created by minded!, I am here to help
    please follow this command for more functions
    /start - to start a conversation
    /clear - to clear past conversation or context
    /help - to get a help menu
    if you need some other thing, let me know :)
    """
    await message.reply(help_command)



@dispatcher.message_handler(commands=['clear'])
async def clear(message:types.Message):
    """
    This handler receives messages with `/clear` command
    """
    clear_past()
    await message.reply("All information are cleared")


@dispatcher.message_handler()
async def main_bot(message:types.Message):
    """
    This handler receives user input and generates responses

    """
    # print(f"USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role":"assistant", "content": reference.response},
            {"role":"user", "content": message.text}

        ]
    )
    reference.response = response['choices'][0]['message']['content']
    # print(f">>>>ChatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)





if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)


