questions = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Paris", "b) New Delhi", "c) Rome", "d) Madrid"],
        "correct_answer": "b"
    },
    {
        "question": "Name the planet nearest to the Earth?",
        "options": ["a) Jupiter", "b) Saturn", "c) Mercury", "d) Mars"],
        "correct_answer": "c"
    },
    {
        "question": "Who invented Radio?",
        "options": ["a) Leonardo da Vinci", "b) Benjamin Frankin", "c) Pablo Picasso", "d) Guglielmo Marconi"],
        "correct_answer": "d"
    },
    {
        "question": "Which is the smallest month of the year?",
        "options": ["a) February", "b) March", "c) April ", "d) May"],
        "correct_answer": "a"
    },
    {
    "question": "Who is the tallest mountain in the world?",
        "options": ["a) Mount Everest", "b) Mount K2", "c) Kangchenjunga", "d) Lhotse"],
        "correct_answer": "a"
    },
]

# Initialize the score
score = 0

# Iterate through each question
for question in questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get user input
    user_answer = input("Enter your answer (a, b, c, or d): ")
    
    # Validate user input and provide feedback
    if user_answer.lower() == question["correct_answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer. The correct answer is:", question["correct_answer"])

# Display the final score
print("Your final score is:", score)