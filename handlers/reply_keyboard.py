from telegram import Update
from telegram.ext import ContextTypes

from quiz_bot import QuizBot
from utils.utils import construct_reply_markup

async def reply_attempt_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz_bot_data: QuizBot) -> None:
    if update.message.text == 'Следующий вопрос':
        pass
    elif update.message.text == quiz_bot_data.correct_answer:
        quiz_bot_data.score += 1
        await update.message.reply_text(text=f'Верно! Правильных ответов: {quiz_bot_data.score}')
    else:
        await update.message.reply_text(text=f'Неправильно! Правильный ответ: {quiz_bot_data.correct_answer}')
            
    quiz_bot_data.update_question()
    await update.message.reply_text(text=quiz_bot_data.current_question, reply_markup=construct_reply_markup(quiz_bot_data))
