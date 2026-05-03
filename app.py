from flask import Flask, request, render_template, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import re
from bson.objectid import ObjectId
import os


app = Flask(__name__)

# MongoDB Atlas connection string
uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["code_snippet_repo"]      # Use your database name
collection = db["snippets"]           # Use your collection name
# Detect category using regex
def detect_category(code):
    if re.search(r'\b(for|while)\b', code):
        return "Loop"
    elif re.search(r'\bif\b.*\belse\b', code):
        return "Conditional"
    elif re.search(r'\bdef\b|\bfunction\b', code):
        return "Function"
    else:
        return "General"

@app.route('/')
def index():
    snippets = list(collection.find())
    return render_template("index.html", snippets=snippets)

@app.route('/add', methods=['POST'])
def add_snippet():
    title = request.form['title']
    code = request.form['code']
    category = detect_category(code)
    collection.insert_one({'title': title, 'code': code, 'category': category})
    return redirect('/')

# ... (all your import and setup code stays the same)

@app.route('/search', methods=['POST'])
def search_snippet():
    query = request.form['query']
    matched = list(collection.find({"code": {"$regex": query, "$options": "i"}}))
    return render_template("index.html", snippets=matched)

# ✅ Move this block ABOVE `if __name__ == '__main__':`
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_snippet(id):
    snippet = collection.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        title = request.form['title']
        code = request.form['code']
        category = detect_category(code)
        collection.update_one({"_id": ObjectId(id)}, {
            "$set": {
                "title": title,
                "code": code,
                "category": category
            }
        })
        return redirect('/')
    return render_template('edit.html', snippet=snippet)

@app.route('/delete/<id>', methods=['GET'])
def delete_snippet(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect('/')

# ✅ This should be the last part of your app
if __name__ == '__main__':
    app.run(debug=True)
