import os
import logging
from openai import AsyncOpenAI # Groq полностью совместим с библиотекой OpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("AI_ENGINE")

class AIBusinessManager:
    def __init__(self):
        # Используем эндпоинт Groq для бесплатных запросов
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    async def generate_response(self, user_text, context=""):
        try:
            # Бесплатная и сверхбыстрая модель Llama 3.3
            response = await self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"Ты — Senior AI Sales Manager. Используй контекст: {context}"},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Groq API Error: {e}")
            return "⚠️ Канал связи с ИИ перегружен. Попробуйте через 30 секунд."
