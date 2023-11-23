from telegram import Update
from telegram.ext import ContextTypes


from quiz_bot import QuizBot
from utils.utils import construct_reply_markup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz_bot_data: QuizBot) -> None:
    """Начинает игру"""
    print(context)
    await update.message.reply_text(text=f'{quiz_bot_data.current_question}', reply_markup=construct_reply_markup(quiz_bot_data))
    
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Завершает игру и прячет клавиатуру"""
    print(context)
    await update.message.reply_text(text=f'Спасибо за игру', reply_markup=construct_reply_markup(None))
