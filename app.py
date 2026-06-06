from flask import Flask, jsonify, request, render_template
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

#load .env file
load_dotenv()

#initial flask
app = Flask(__name__)

#establish MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["booktracker"]
collection = db["pythonModule_books"]

#test if connection is successful
try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

#Home route
@app.route('/')
def home():
    books = list(collection.find())
    for book in books:
        book["id"] = str(book["_id"]) # Convert ObjectId to string for easier handling in templates
    return render_template('index.html', books=books)

@app.route("/add")
def add_page():
    return render_template("add_books.html")


@app.route("/book/<id>")
def book_detail(id: str):
    book = collection.find_one({"_id": ObjectId(id)})
    book["id"] = str(book["_id"])
    return render_template("book_details.html", book=book)