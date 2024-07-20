import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardManager:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        self.flashcards.append(Flashcard(question, answer))

    def review_flashcards(self):
        if not self.flashcards:
            print("No flashcards to review.")
            return

        for flashcard in self.flashcards:
            print(f"Q: {flashcard.question}")
            input("Press Enter to see the answer...")
            print(f"A: {flashcard.answer}\n")

    def quiz_flashcards(self):
        if not self.flashcards:
            print("No flashcards to quiz.")
            return

        random.shuffle(self.flashcards)
        for flashcard in self.flashcards:
            print(f"Q: {flashcard.question}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!\n")
            else:
                print(f"Wrong. The correct answer is: {flashcard.answer}\n")

def main():
    manager = FlashcardManager()
    while True:
        print("Flashcard App")
        print("1. Add a flashcard")
        print("2. Review flashcards")
        print("3. Quiz yourself")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            manager.add_flashcard(question, answer)
            print("Flashcard added!\n")
        elif choice == '2':
            manager.review_flashcards()
        elif choice == '3':
            manager.quiz_flashcards()
        elif choice == '4':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
