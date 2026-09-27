from flask import Flask,request,render_template,redirect,url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os

load_dotenv()
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
    app.run(debug=True)