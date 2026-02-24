import aiohttp
import logging
from core.config import GEMINI_API_KEY

logger = logging.getLogger("AI_ENGINE")

class AIBusinessManager:
    def __init__(self):
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    async def generate_response(self, user_text, context=""):
        system_prompt = (
            "Ты — AI-сотрудник компании. Твоя цель: помогать клиентам на основе контекста.\n"
            f"Контекст компании: {context}\n\n"
            f"Запрос клиента: {user_text}"
        )
        
        payload = {
            "contents": [{"parts": [{"text": system_prompt}]}]
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.api_url, json=payload) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data['candidates'][0]['content']['parts'][0]['text']
                    return "Прошу прощения, я сейчас на техобслуживании. Попробуйте позже."
            except Exception as e:
                logger.error(f"AI Error: {e}")
                return "Ошибка связи с интеллектом."
