from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask import jsonify
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'message': 'Invalid token', 
                    'error': error}), 401

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({'message': 'Unauthorized', 
                    'error': error}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({'message': 'Token expired'}), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_data):
    return jsonify({'message': 'Token revoked'}), 401
