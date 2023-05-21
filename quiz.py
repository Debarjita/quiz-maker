import random

class Quiz:
    def __init__(self):              #authentication of the user using this method.
        self.quizzes = {}
        self.scores = {}

    def create_quiz(self, user, title, questions):
        if user not in self.quizzes:
            self.quizzes[user] = {}

        self.quizzes[user][title] = questions

    def submit_quiz(self, user, title, score):
        if user not in self.scores:
            self.scores[user] = {}

        self.scores[user][title] = score

    def get_quiz(self, user, title):
        if user in self.quizzes and title in self.quizzes[user]:
            return self.quizzes[user][title]
        return None

    def show_leaderboard(self):
        if not self.scores:
            print("No scores available.")
            return

        sorted_scores = sorted(self.scores.items(), key=lambda x: sum(x[1].values()), reverse=True)
        print("Leaderboard:")

        for user, quiz_scores in sorted_scores:
            total_score = sum(quiz_scores.values())
            print(f"User: {user}, Total Score: {total_score}")
            for quiz, score in quiz_scores.items():
                print(f"Quiz: {quiz}, Score: {score}")
            print()


def take_quiz_randomly():
    user = input("Enter your username: ")
    title = input("Enter the quiz title: ")

    quiz.create_quiz(user, title, [])

    questions = []
    num_questions = int(input("Enter the number of questions: "))

    for i in range(num_questions):
        question = input(f"Enter question {i + 1}: ")
        options = input("Enter the multiple-choice options (comma-separated): ").split(",")
        correct_answer = input("Enter the correct answer (index of the correct option): ")
        questions.append((question, options, correct_answer))

    random.shuffle(questions)  # Shuffle the questions

    quiz.quizzes[user][title] = questions
    print("Quiz created successfully!")

    score = 0
    total_questions = len(questions)

    for i, (question, options, correct_answer) in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        print("Options:")
        for j, option in enumerate(options, start=1):
            print(f"{j}. {option}")

        user_answer = input("Enter your answer (index of the chosen option): ")

        if user_answer == correct_answer:
            score += 1

        print()

    final_score = (score / total_questions) * 100
    quiz.submit_quiz(user, title, final_score)
    print("Quiz submitted successfully!")
    print(f"Your score: {final_score}%")


def main():
    global quiz
    quiz = Quiz()

    while True:
        print("1. Create a quiz")
        print("2. Get a quiz")
        print("3. Take a quiz randomly")
        print("4. Submit a quiz")
        print("5. Show leaderboard")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            take_quiz_randomly()

        elif choice == "2":
            user = input("Enter your username: ")
            title = input("Enter the quiz title: ")

            quiz_data = quiz.get_quiz(user, title)
            if quiz_data:
                print("Quiz:")
                print("Title:", title)
                print("Questions:")
                for i, (question, options, _) in enumerate(quiz_data, start=1):
                    print(f"{i}. {question}")
                    print("Options:", ", ".join(options))
                    print()
            else:
                print("Quiz not found!")

        elif choice == "3":
            take_quiz_randomly()

        elif choice == "4":
            user = input("Enter your username: ")
            title = input("Enter the quiz title: ")
            score = float(input("Enter your score: "))

            quiz.submit_quiz(user, title, score)
            print("Quiz submitted successfully!")

        elif choice == "5":
            quiz.show_leaderboard()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
