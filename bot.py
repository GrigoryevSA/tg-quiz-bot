from functools import partial

from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

import config
from quiz_bot import QuizBot
from utils.utils import construct_reply_markup
import handlers


def main() -> None:
    # Создаём приложение и передаём ему токен нашего бота
    application = Application.builder().token(config.token).build()
    
    # Создаём объект, который хранит в себе информацию о текущем вопросе
    qbot = QuizBot()
    
    # Создаём обработчики команд и сообщений
    start_handler = partial(handlers.start, quiz_bot_data=qbot)
    reply_handler = partial(handlers.reply_attempt_handler, quiz_bot_data=qbot)

    # Регистрируем обработчики для команд /start и /stop
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("stop", handlers.stop))
    
    # Для состоящих из текста и не являющихся командами добавляем echo как обработчик
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_handler))
    
    # Запускаем бота до тех пор пока пользователь не нажмёт ctrl+C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
