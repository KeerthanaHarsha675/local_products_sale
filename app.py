"""
=========================================================
HeritageHandcrafts - Main Flask Application
=========================================================

This file is the entry point of the backend.

Responsibilities:
- Create Flask application
- Load configuration
- Initialize database
- Enable CORS
- Register all route blueprints
- Create upload folders (if not present)
- Run the Flask server
"""

import os

from flask import Flask
from flask_cors import CORS

from config import Config

# -----------------------------
# Import Database
# -----------------------------
from models import db

from middleware.jwt_manager import initialize_jwt

# -----------------------------
# Import Route Blueprints
# -----------------------------
from routes.admin_routes import admin_bp
from routes.artisan_routes import artisan_bp
from routes.auth_routes import auth_bp
from routes.customer_routes import customer_bp
from routes.product_routes import product_bp
from routes.gi_routes import gi_bp
from routes.ai_routes import ai_bp

# =========================================================
# Create Flask Application
# =========================================================
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize SQLAlchemy
db.init_app(app)

initialize_jwt(app)


# =========================================================
# Create Upload Directories
# =========================================================
UPLOAD_FOLDERS = [
    "uploads/products",
    "uploads/artisan_profiles",
    "uploads/gi_certificates",
    "uploads/temp",
]

for folder in UPLOAD_FOLDERS:
    os.makedirs(folder, exist_ok=True)


# =========================================================
# Register Blueprints
# =========================================================
app.register_blueprint(auth_bp, url_prefix="/api/auth")

app.register_blueprint(admin_bp, url_prefix="/api/admin")

app.register_blueprint(artisan_bp, url_prefix="/api/artisan")

app.register_blueprint(customer_bp, url_prefix="/api/customer")

app.register_blueprint(product_bp, url_prefix="/api/products")

app.register_blueprint(gi_bp, url_prefix="/api/gi")

app.register_blueprint(ai_bp, url_prefix="/api/ai")

# =========================================================
# Home Route
# =========================================================
@app.route("/")
def home():
    return {
        "message": "Welcome to HeritageHandcrafts Backend",
        "status": "Running"
    }


# =========================================================
# Run Server
# =========================================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )