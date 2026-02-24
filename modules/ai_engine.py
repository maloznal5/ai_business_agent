import os
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("AI_ENGINE")

class AIBusinessManager:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def generate_response(self, user_text, context=""):
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": f"Ты — Senior AI Sales Manager. Используй контекст компании: {context}"},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI Error: {e}")
            return "⚠️ Системная ошибка AI. Инженеры уже уведомлены."
