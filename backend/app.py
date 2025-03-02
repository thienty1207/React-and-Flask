import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
database_url = os.getenv("DATABASE_URL", "postgresql://postgres:tohkaty01@localhost:5432/friend")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import models để db.create_all() có thể tạo bảng
from models import Friend

# Import routes sau khi đã khởi tạo app, db và models
import routes

# Tạo bảng trong database trong application context
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
