class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        total_question = len(self.question_list)
        return self.question_number < total_question

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # print(current_question)

        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")   # not current_question["text"]
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")