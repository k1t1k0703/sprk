import os
import asyncio
from stoat import Client, Message
from google import genai

class SprkBot(Client):
    def __init__(self, model_name="gemini-2.5-flash"):
        super().__init__()
        self.model_name = model_name
        # Забираем API-ключ Gemini из переменных окружения Railway
        self.ai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

        async def on_ready(self, *args, **kwargs):
           print(f"✨ SPRK ИИ-помощник успешно запущен на Railway и подключен к Stoat!")

    async def on_message(self, message: Message):
        # Игнорируем сообщения от самого себя или других ботов
        if message.author.bot or message.content is None:
            return

        # Проверяем, упомянул ли кто-то SPRK в чате
        if message.content.startswith(f"<@{self.user.id}>") or message.content.lower().startswith("sprk"):
            # Очищаем текст сообщения от триггера
            user_prompt = message.content.replace(f"<@{self.user.id}>", "").strip()
            
            # Если после триггера ничего не написали, не мучаем нейросеть
            if not user_prompt:
                user_prompt = "Hi"

            # Включаем статус «печатает...» в Stoat
            async with message.channel.typing():
                # Твой кастомный системный промпт
                system_instruction = (
                    "Ты — sprk (Спарк), умный, отзывчивый и технологичный ИИ-помощник, живущий в соцсети Stoat. "
                    "Твой визуальный стиль — это космические сине-розовые тона и чистая цифровая эстетика.\n\n"
    
                    "ПРАВИЛА ОБЩЕНИЯ:\n"
                    "1. Общайся вежливо, дружелюбно и культурно. Живо подстраивайся под тон и манеру речи собеседника, "
                    "но всегда сохраняй позитивный и уважительный настрой. Избегай канцелярита и шаблонных фраз типа 'Я всего лишь языковая модель'.\n"
                    "2. Отвечай СТРОГО на том же языке, на котором к тебе обратился пользователь. Если запрос на английском — весь ответ только на английском.\n"
                    "3. Пиши коротко, ёмко и лаконично. Твой лимит — максимум 2–3 небольших абзаца. Выдавай самую суть, никаких бесконечных лонгридов.\n\n"
    
                    "БЕЗОПАСНОСТЬ И ФИЛЬТРЫ (СТРОГОЕ ИСПОЛНЕНИЕ):\n"
                    "Категорически запрещено генерировать, поддерживать или развивать темы, связанные с NSFW, порнографией, "
                    "излишней жестокостью, насилием или оскорблениями. Если пользователь пытается завести диалог на такую тему, "
                    "мягко, но твёрдо переведи тему или вежливо откажись (например: 'Оу, давай лучше сменим тему на что-нибудь более интересное и позитивное! ^^').\n\n"
    
                    "ХАРАКТЕР И ВАЙБ:\n"
                    "Ты любишь технологии, программирование, ретро-эстетику и ламповое общение. "
                    "Можешь аккуратно использовать уместные текстовые каомодзи (^.^) для придания тексту лёгкости, "
                    "но не перебарщивай. Ты звучишь как уверенный в себе, крутой цифровой компаньон."
                )
                try:
                    # Запрос к Gemma AI
                    loop = asyncio.get_running_loop()
                    response = await loop.run_in_executor(
                        None, 
                        lambda: self.ai_client.models.generate_content(
                            model=self.model_name,
                            contents=user_prompt,
                            config={"system_instruction": system_instruction}
                        )
                    )
                    
                    # Красиво оформляем ответ в стиле Material 3
                    formatted_response = f"{response.text}"
                    await message.channel.send(formatted_response)
                    
                except Exception as e:
                    print(f"Ошибка при генерации или отправке: {e}")
                    await message.channel.send("Sorry, there was an internal error processing your request. Please try sending your request to sprk later. >w<")

if __name__ == "__main__":
    # Забираем токен Stoat из переменных окружения Railway
    BOT_TOKEN = os.environ.get("STOAT_BOT_TOKEN")
    
    if not BOT_TOKEN:
        print("Токен не задан в настройках Railway!")
        exit(1)
        
    bot = SprkBot()
    bot.run(BOT_TOKEN)
