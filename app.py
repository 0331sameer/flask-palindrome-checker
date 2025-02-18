from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(word):
    return word == word[::-1]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        word = request.form.get("word").strip().lower()
        if word:
            result = is_palindrome(word)
    return render_template("index.html", result=result, word=word if 'word' in locals() else "")

if __name__ == "__main__":
    app.run(debug=True)
