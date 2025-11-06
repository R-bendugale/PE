from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    taste = request.form["taste"]
    diet = request.form["diet"]
    mood = request.form["mood"]

    # Rule-based logic (Expert System)
    if taste == "spicy" and diet == "veg":
        suggestion = "Indian Veg Restaurant 🍛"
    elif taste == "spicy" and diet == "nonveg":
        suggestion = "Indian Non-Veg Dhaba 🍗"
    elif taste == "sweet":
        suggestion = "Dessert Café 🍰"
    elif taste == "salty":
        suggestion = "Fast Food Corner 🍟"
    elif mood == "happy":
        suggestion = "Candle Light Restaurant 💖"
    elif mood == "party":
        suggestion = "Club & Grill 🍹"
    else:
        suggestion = "Family Dining Restaurant 🍽️"

    return render_template("index.html", result=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
