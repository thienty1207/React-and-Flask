from app import app, db
from flask import request, jsonify
from models import Friend

# Route gốc
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is working!"})

# Route /api/friends để lấy tất cả bạn bè
@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

# Route để tạo bạn bè mới
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")
        
        # FETCH avatar image based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None

        new_friend = Friend(
            name=name,
            role=role,
            description=description,
            gender=gender,
            img_url=img_url
        )

        db.session.add(new_friend)
        db.session.commit()
        return jsonify(new_friend.to_json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500









