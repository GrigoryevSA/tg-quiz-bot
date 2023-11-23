import random

import models

class QuizBot:
    def __init__(self) -> None:
        self.current_question = ""
        self.answers = list()
        self.correct_answer = ""
        self.score = 0
        self.update_question()
    
    def update_question(self) -> None:
        q = models.Question()
        self.current_question, self.answers, self.correct_answer = q.query_random_question()
