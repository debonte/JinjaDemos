from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return "<p>Hello, World!</p>"

class Cat:
    def __init__(self, name: str, age: int, colors: list[str]):
        self.name = name
        """Name of the cat."""
        
        self.age = age
        """Age in years."""

        self.colors = colors
        """List of colors the cat has."""

cats = [Cat("Mittens", 10, ["black", "white"]), Cat("Max", 8, ["gray"]), Cat("Watson", 1, ["black", "white"]), Cat("Sherlock", 1, ["gray", "white"])]

@app.route("/items/<id>")
def read_item(id: str):
    return render_template("subdir/item.html", id=id, cats=cats, dogOpinion2="annoying!")

