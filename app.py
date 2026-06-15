from flask import Flask, render_template, request

app = Flask(__name__)

def answer_question(question):
    question = question.lower()

    if "capital of france" in question:
        return "Paris is the capital of France."

    elif "capital of india" in question:
        return "New Delhi is the capital of India."

    elif "python" in question:
        return "Python is a popular programming language."

    elif "ai" in question:
        return "AI stands for Artificial Intelligence."

    else:
        return "Sorry, I don't know the answer."

def summarize_text(text):
    words = text.split()

    if len(words) > 20:
        return " ".join(words[:20]) + "..."
    else:
        return text

def generate_creative_content(topic):
    return f"""
    Once upon a time, there was a story about {topic}.
    The journey of {topic} inspired many people.
    In the end, {topic} became a symbol of success and hope.
    """

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        task = request.form["task"]
        user_input = request.form["user_input"]

        if task == "question":
            result = answer_question(user_input)

        elif task == "summary":
            result = summarize_text(user_input)

        elif task == "creative":
            result = generate_creative_content(user_input)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)