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

#-------------------- Flask route
@app.route('/')
def home() -> str:
    books = list(collection.find())
    for book in books:
        book["id"] = str(book["_id"]) # Convert ObjectId to string for easier handling in templates
    return render_template('index.html', books=books)

@app.route("/add")
def add_page() -> str:
    return render_template("add_books.html")


@app.route("/book/<id>")
def book_detail(id: str) -> str:
    book = collection.find_one({"_id": ObjectId(id)})
    book["id"] = str(book["_id"])
    return render_template("book_details.html", book=book)

#-------------------- API routes
#fetch all books as JSON
@app.route("/api/books", methods=["GET"])
def get_books() -> tuple:
    books = list(collection.find())
    for book in books:
        book["id"] = str(book["_id"])
        del book["_id"] # we delete the ObjectID  so that it doesn't cause issues with Jsonify
    return jsonify(books), 200

@app.route("/api/books", methods=["POST"])
def add_book() -> tuple:
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"message": "Book added!", "id": str(result.inserted_id)}), 201

@app.route("/api/books/<id>", methods=["PUT"])
def update_book(id: str) -> tuple:
    data = request.get_json()
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Book updated!"}), 200

@app.route("/api/books/<id>", methods=["DELETE"])
def delete_book(id: str) -> tuple:
    collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Book deleted!"}), 200

if __name__ == "__main__":
    app.run(debug=False)