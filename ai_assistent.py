def answer_question():
    question = input("Enter your question: ").lower()

    if "capital of france" in question:
        print("Answer: Paris is the capital of France.")

    elif "capital of india" in question:
        print("Answer: New Delhi is the capital of India.")

    elif "python" in question:
        print("Answer: Python is a popular programming language.")

    elif "ai" in question:
        print("Answer: AI stands for Artificial Intelligence.")

    else:
        print("Answer: Sorry, I don't know the answer.")


def summarize_text():
    text = input("Enter text to summarize: ")

    words = text.split()

    if len(words) > 20:
        summary = " ".join(words[:20]) + "..."
    else:
        summary = text

    print("\nSummary:")
    print(summary)


def generate_creative_content():
    topic = input("Enter a topic: ")

    print("\nCreative Content:")
    print(f"Once upon a time, there was a story about {topic}.")
    print(f"The journey of {topic} inspired many people.")
    print(f"In the end, {topic} became a symbol of success and hope.")


while True:

    print("\n===== AI ASSISTANT =====")
    print("1. Answer Questions")
    print("2. Summarize Text")
    print("3. Generate Creative Content")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        answer_question()

    elif choice == "2":
        summarize_text()

    elif choice == "3":
        generate_creative_content()

    elif choice == "4":
        print("Thank you for using AI Assistant!")
        break

    else:
        print("Invalid choice!")
        continue

    feedback = input("\nWas this response helpful? (yes/no): ")

    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")

    print("Feedback saved successfully!")