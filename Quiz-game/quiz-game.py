questions = {
    "What is the capital of France?": "Paris",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is 2 + 2?": "4"
}

def quiz_game():
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")
    print(f"\nQuiz over! Your score is {score} out of {len(questions)}.")

# Usage
quiz_game()
