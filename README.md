# 📚 Book Tracker

A simple web application built with Flask and MongoDB that allows users to manage their personal book collection.

## 👥 Team

| Member | GitHub |
|--------|--------|
| Erfan Moadeli | [@mdl-erfan](https://github.com/mdl-erfan) |
| Tanisha Patel | [@Tanishqptl](https://github.com/Tanishqptl) |


---

## 🚀 Features

- View all books in your collection
- Add a new book with title, author, genre, status, rating and notes
- View detailed information about each book
- Delete a book from the collection
- REST API with JSON responses

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python + Flask |
| Database | MongoDB Atlas |
| Frontend | HTML + CSS |
| Deployment | Render.com |

---

## 📁 Project Structure

```
book-tracker/
├── app.py              # Flask application and routes
├── requirements.txt    # Project dependencies
├── .gitignore          # Files to ignore in Git
├── render.yaml         # Render deployment config
├── README.md           # Project documentation
├── static/
│   └── style.css       # Stylesheet
└── templates/
    ├── index.html       # Home page
    ├── add_books.html   # Add book form
    └── book_details.html # Book detail page
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Tanishqptl/books.git
cd books
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory
```
MONGO_URI=your_mongodb_atlas_connection_string
```

### 5. Run the application
```bash
python app.py
```

### 6. Open your browser
```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | Get all books |
| POST | `/api/books` | Add a new book |
| PUT | `/api/books/<id>` | Update a book |
| DELETE | `/api/books/<id>` | Delete a book |

---

## 📖 Pages

| Route | Description |
|-------|-------------|
| `/` | Home page — displays all books |
| `/add` | Form to add a new book |
| `/book/<id>` | Detail page for a single book |

---

## 🚀 Deployment

The app is deployed on **Render.com** and uses **MongoDB Atlas** as the cloud database.

Live URL: https://book-tracker-r7t6.onrender.com

---
