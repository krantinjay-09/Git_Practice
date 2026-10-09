<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import pymongo
=======
from flask import Flask,request,render_template,redirect,url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
>>>>>>> 72b7dcf25481efae9277cfe518b6016cbd9b1d24
from dotenv import load_dotenv
import os

load_dotenv()
<<<<<<< HEAD

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
=======
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

db = client["signupDB"]
collection = db["users"]

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    if len(password) < 4:
        error = "Password must be at least 4 characters long."
        return render_template('form.html', error=error)
    
    try:
        collection.insert_one({"name": name, "email": email, "password": password})
        return redirect(url_for('success'))
    except PyMongoError as e:
        return render_template('form.html', error="Database error: " + str(e))
    

@app.route('/success')
def success():
    return "Data submitted successfully!"


if __name__ == '__main__':
>>>>>>> 72b7dcf25481efae9277cfe518b6016cbd9b1d24
    app.run(debug=True)