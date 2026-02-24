import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from core.config import TOKEN
from modules.ai_engine import AIBusinessManager

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()
ai_manager = AIBusinessManager()

# База знаний (симуляция RAG)
BUSINESS_CONTEXT = "Мы продаем услуги автоматизации бизнеса на Python. Стек: aiogram, n8n, Flask. Цены от 5000 грн."

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🤖 Здравствуйте! Я ваш AI-ассистент. Задайте мне любой вопрос по нашим услугам.")

@dp.message()
async def handle_ai_chat(message: types.Message):
    # Визуальный эффект "печатает"
    await bot.send_chat_action(message.chat.id, "typing")
    response = await ai_manager.generate_response(message.text, BUSINESS_CONTEXT)
    await message.answer(response)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
