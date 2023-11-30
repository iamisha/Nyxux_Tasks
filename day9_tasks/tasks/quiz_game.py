""" 

"""

import json


class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class QuizGame:
    def __init__(self, questions_file):
        with open(questions_file, 'r') as f:
            self.questions = json.load(f)

    def play_game(self, player):
        for question in self.questions:
            self.show_question(question)
            answer = input("Enter your answer: ")
            if answer == question['correct_answer']:
                player.score += 1
                print("Correct!")
            else:
                print("Incorrect. The correct answer is", question['correct_answer'])

        print("Your final score is:", player.score)


    def show_question(self, question):
        print("----------------------------------------------------------------")
        print(question['question_text'])
        for option in question['options']:
            print(option)


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = Player(player_name)

    quiz_game = QuizGame("questions.json")
    quiz_game.play_game(player)
