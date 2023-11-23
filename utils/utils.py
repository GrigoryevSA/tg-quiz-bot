from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from quiz_bot import QuizBot


def construct_reply_markup(qbot: QuizBot) -> ReplyKeyboardMarkup:
    if not qbot:
        return ReplyKeyboardRemove()
    keyboard = list()
    keyboard.append([])
    for button_name in qbot.answers:
        keyboard[0].append(KeyboardButton(f"{button_name}"))
        
    keyboard.append([KeyboardButton(f"Следующий вопрос")])
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
