from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
jwt = JWTManager(app)
CORS(app)

# User Model
class User:
    collection = mongo.db.users
    
    @staticmethod
    def create(username, email, password, role="user"):
        hashed_password = generate_password_hash(password)
        user = {
            "username": username,
            "email": email,
            "password": hashed_password,
            "role": role,
            "createdAt": datetime.datetime.utcnow()
        }
        return User.collection.insert_one(user)
    
    @staticmethod
    def find_by_email(email):
        return User.collection.find_one({"email": email})
    
    @staticmethod
    def find_by_id(user_id):
        return User.collection.find_one({"_id": ObjectId(user_id)})
    
    @staticmethod
    def check_password(user, password):
        return check_password_hash(user["password"], password)
    
    @staticmethod
    def get_all():
        return list(User.collection.find())
    
    @staticmethod
    def delete(user_id):
        return User.collection.delete_one({"_id": ObjectId(user_id)})

# Item Model
class Item:
    collection = mongo.db.items
    
    @staticmethod
    def create(title, description, price, created_by):
        item = {
            "title": title,
            "description": description,
            "price": float(price),
            "createdBy": ObjectId(created_by),
            "createdAt": datetime.datetime.utcnow()
        }
        return Item.collection.insert_one(item)
    
    @staticmethod
    def find_all():
        return list(Item.collection.find())
    
    @staticmethod
    def find_by_id(item_id):
        return Item.collection.find_one({"_id": ObjectId(item_id)})
    
    @staticmethod
    def update(item_id, data):
        update_data = {}
        if "title" in data:
            update_data["title"] = data["title"]
        if "description" in data:
            update_data["description"] = data["description"]
        if "price" in data:
            update_data["price"] = float(data["price"])
        return Item.collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    
    @staticmethod
    def delete(item_id):
        return Item.collection.delete_one({"_id": ObjectId(item_id)})

# Auth Routes
@app.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400
    
    if User.find_by_email(email):
        return jsonify({"error": "Email already exists"}), 400
    
    User.create(username, email, password)
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    user = User.find_by_email(email)
    if not user or not User.check_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=str(user["_id"]), additional_claims={"role": user["role"]})
    return jsonify({"access_token": access_token, "user": {"id": str(user["_id"]), "username": user["username"], "role": user["role"]}}), 200

# Profile Routes
@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "role": user["role"],
        "createdAt": user["createdAt"].isoformat()
    }), 200

# Item Routes
@app.route("/add-item", methods=["POST"])
@jwt_required()
def add_item():
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    price = data.get("price")
    
    if not title or not price:
        return jsonify({"error": "Missing required fields"}), 400
    
    result = Item.create(title, description, price, user_id)
    return jsonify({"message": "Item created successfully", "id": str(result.inserted_id)}), 201

@app.route("/browse", methods=["GET"])
def browse_items():
    items = Item.find_all()
    for item in items:
        item["_id"] = str(item["_id"])
        item["createdBy"] = str(item["createdBy"])
        item["createdAt"] = item["createdAt"].isoformat()
    return jsonify(items), 200

@app.route("/item/<id>", methods=["GET"])
def item_detail(id):
    item = Item.find_by_id(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    item["_id"] = str(item["_id"])
    item["createdBy"] = str(item["createdBy"])
    item["createdAt"] = item["createdAt"].isoformat()
    return jsonify(item), 200

@app.route("/item/<id>", methods=["PUT"])
@jwt_required()
def update_item(id):
    user_id = get_jwt_identity()
    item = Item.find_by_id(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    if str(item["createdBy"]) != user_id:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.get_json()
    Item.update(id, data)
    return jsonify({"message": "Item updated successfully"}), 200

@app.route("/item/<id>", methods=["DELETE"])
@jwt_required()
def delete_item(id):
    user_id = get_jwt_identity()
    item = Item.find_by_id(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    if str(item["createdBy"]) != user_id:
        return jsonify({"error": "Unauthorized"}), 403
    
    Item.delete(id)
    return jsonify({"message": "Item deleted successfully"}), 200

# Admin Routes
@app.route("/admin/users", methods=["GET"])
@jwt_required()
def get_users():
    claims = get_jwt()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    users = User.get_all()
    for user in users:
        user["_id"] = str(user["_id"])
        user["createdAt"] = user["createdAt"].isoformat()
        del user["password"]
    return jsonify(users), 200

@app.route("/admin/users/<id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    claims = get_jwt()
    if claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    if User.find_by_id(id):
        User.delete(id)
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])