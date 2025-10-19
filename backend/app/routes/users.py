# app/routes/users.py
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..services.user_service import (
    create_user, get_user_by_id, get_all_users,
    update_user, delete_user
)

users_bp = Blueprint("users", __name__)
CORS(users_bp)

@users_bp.route("/register", methods=["POST"])
def create():
    data = request.get_json() or {}
    username = data.get("username")
    nama = data.get("nama")
    email = data.get("email")
    password = data.get("password")

    if not all([nama, username, email, password]):
        return jsonify({"error": "name, email, and password are required"}), 400

    user = create_user(nama, username, email, password)
    if not user:
        return jsonify({"error": "email already exists"}), 400

    return jsonify(user.to_dict()), 201

@users_bp.route("/data", methods=["GET"])
def list_users():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    pagination = get_all_users(page, per_page)
    items = [u.to_dict() for u in pagination.items]
    return jsonify({
        "items": items,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total
    }), 200

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "not found"}), 404
    return jsonify(user.to_dict()), 200

@users_bp.route("/<int:user_id>", methods=["PUT", "PATCH"])
def edit_user(user_id):
    data = request.get_json() or {}
    user = update_user(user_id, **data)
    if not user:
        return jsonify({"error": "Data Tidak Ada"}), 404
    return jsonify({
        "message": "Data user berhasil diperbarui",
        "user": user.to_dict()    
    }), 200

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    ok = delete_user(user_id)
    if not ok:
        return jsonify({"error": "Data Tidak Ada"}), 404
    return jsonify({
            
    }), 204
