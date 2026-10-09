from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["todo_db"]
items = db["items"]


@app.route("/")
def index():
    # get all saved items and show them on the page
    all_items = list(items.find())
    return render_template("index.html", items=all_items)


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName", "").strip()
    item_description = request.form.get("itemDescription", "").strip()

    # name is required, description can be empty
    if item_name == "":
        return "Item name is required", 400

    items.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)