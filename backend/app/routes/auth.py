from flask import Blueprint, request, jsonify, current_app
from flask_cors import CORS
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity, set_refresh_cookies, set_access_cookies, unset_jwt_cookies
)
from ..services.user_service import authenticate_user, get_user_by_id, create_user



auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"message": "username and password are required"}), 400
    
    user = authenticate_user(username, password)
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    
    addintional_claims = {"username": user.username}
    access_token = create_access_token(identity=user.id, additional_claims=addintional_claims)
    refresh_token = create_refresh_token(identity=user.id)
    
    return jsonify({
        "message": "Login Berhasil",
        "access_token": access_token,
        "user": user.to_dict()
    }), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get("username")
    nama = data.get("nama")
    email = data.get("email")
    password = data.get("password")

    if not all([nama, username, email, password]):
        return jsonify({"error": "name, email, dan password tidak boleh kosong"}), 400

    user = create_user(nama, username, email, password)
    if not user:
        return jsonify({"error": "email sudah ada"}), 400

    return jsonify({
        "message": "Registrasi berhasil",
        "user": user.to_dict()    
    }), 201

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user_id = get_jwt_identity()
    addintional_claims = {}
    new_access_token = create_access_token(identity=current_user_id, additional_claims=addintional_claims)
    return jsonify({"access_token": new_access_token}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user_id = get_jwt_identity()
    user = get_user_by_id(current_user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"user": user.to_dict()}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200