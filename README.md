📌 Code Snippet Repository

A full-stack web application built with Flask and MongoDB that allows users to store, search, edit, and categorize programming code snippets efficiently using regex-based classification.

🧠 Features
➕ Add code snippets with title and code
🔍 Search snippets using keyword matching
🧾 Automatic category detection using Regex:
Loop
Conditional
Function
General
✏️ Edit existing snippets
🗑️ Delete snippets
📂 Organized template-based UI (Flask Jinja2)
☁️ MongoDB Atlas cloud database integration
🌐 Deployed on Render
🛠️ Tech Stack
Frontend: HTML, CSS (Jinja2 Templates)
Backend: Flask (Python)
Database: MongoDB Atlas
Libraries:
PyMongo
Regex (re module)
BSON (ObjectId)
Deployment: Render


📁 Project Structure
code-snippet-repo/
│
├── app.py
├── requirements.txt
├── Procfile
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── edit.html
└── .gitignore



⚙️ Installation & Setup (Local)
1. Clone repository
git clone https://github.com/your-username/code-snippet-repo.git
cd code-snippet-repo
2. Create virtual environment
python -m venv venv
3. Activate environment
venv\Scripts\activate   # Windows
4. Install dependencies
pip install -r requirements.txt
5. Run application
python app.py



🌐 Environment Variables

Create a .env file (for local use):

MONGO_URI=your_mongodb_atlas_connection_string


🚀 Deployment (Render)
Push project to GitHub
Connect repository to Render
Set:
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Add Environment Variable:
MONGO_URI


📊 How It Works
User adds a code snippet
Regex analyzes code:
detects loops, conditions, functions
Category is automatically assigned
Data is stored in MongoDB Atlas
Users can search, edit, or delete snippets
🎯 Future Improvements
🔐 User authentication system
🏷️ Tag-based filtering
📊 Analytics dashboard
🌙 Dark mode UI
📱 Mobile responsive design improvements
🔗 REST API version


👨‍💻 Author

Syed Saad Raza

💻 Computer Science Student
🤖 Interested in AI, ML, and Full Stack Development
📌 Focused on building real-world projects
⭐ If you like this project

Give it a star ⭐ on GitHub and feel free to contribute!
