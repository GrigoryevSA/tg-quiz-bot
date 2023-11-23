import random

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///./questions_new.db')
DbSession = scoped_session(sessionmaker(bind=engine))


class Question(Base):
    """модель для таблицы Вопросов"""
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    alternative = Column(String)
    
    def query_random_question(self):
        """Метод для получения случайного вопроса из таблицы Вопросов"""
        q = Question()
        question_list = q._query_questions()
        question = question_list[random.randrange(len(question_list))]
        next_question = question.question
        answers = question.alternative.split(',')
        answers.append(question.answer)
        random.shuffle(answers)
        return next_question, answers, question.answer 

    
    def _query_questions(self):
        res = list()
        with DbSession() as session:
            questions = select(Question)
            for question in session.scalars(questions):
                print(question.question, question.answer, question.alternative)
                res.append(question)
        return res               
    
Base.metadata.create_all(engine)

# Код для добавления вопросов в БД
# with DbSession() as session:
#     q1 = Question(
#         question="На каком языке мы пишем бота?",
#         answer="python",
#         alternative="C++, English, Telegram"
#     )

#     q2 = Question(
#         question="Какую библиотеку мы используем для написания бота?",
#         answer="python-telegram-bot",
#         alternative="aiogram, pyrogram, telethone"
#     )

#     questions = select(Question)
#     for question in session.scalars(questions):
#         print(question.question, question.answer, question.alternative)
