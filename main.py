import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='7171706649:AAG34PX6t0nNtkr17ULZY8aogUO1JrsRrIE')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!')
    await message.reply('How are you?')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("You've pressed help button")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is shutdown')
