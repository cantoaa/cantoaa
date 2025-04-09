
class QuizBrain:
    def __init__(self, questlist):
        self.question_number = 0
        self.questionlist = questlist
    def havequestions(self):
            return self.question_number < len(self.questionlist)
    def next_question(self):
        current_question = self.questionlist[self.question_number]
        self.question_number += 1
        if input(f"Q. {self.question_number}: {current_question.text}(True/False): ") == current_question.answer:
            return True
        else:
            return False
        

        
        
