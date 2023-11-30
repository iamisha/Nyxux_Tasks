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
            answer = input("Enter your answer (1, 2, 3, 4): ")

            # Convert answer to an integer for comparison
            answer = int(answer) if answer.isdigit() else None

            if answer is not None and 1 <= answer <= len(question['options']):
                if question['options'][answer - 1] == question['correct_answer']:
                    player.score += 1
                    print("Correct!")
                else:
                    print("Incorrect. The correct answer is", question['correct_answer'])
            else:
                print("Invalid input. Please enter a valid option.")

        print("Your final score is:", player.score)

    def show_question(self, question):
        print("----------------------------------------------------------------")
        print(question['question_text'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = Player(player_name)

    quiz_game = QuizGame("questions.json")
    quiz_game.play_game(player)
