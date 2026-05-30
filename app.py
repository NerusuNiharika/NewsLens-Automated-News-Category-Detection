from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["news"]

    transformed_text = vectorizer.transform([text])

    prediction = model.predict(transformed_text)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)