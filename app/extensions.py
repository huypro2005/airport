from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'message': 'Invalid token', 
                    'error': error,
                    'status': 'fail'}), 401

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({'message': 'Unauthorized', 
                    'error': error,
                    'status': 'fail'}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({'message': 'Token expired',
                    'status': 'fail'}), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_data):
    return jsonify({'message': 'Token revoked',
                    'status': 'fail'}), 401
