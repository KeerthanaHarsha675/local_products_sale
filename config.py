"""
=========================================================
HeritageHandcrafts - Configuration File
=========================================================

This file stores all application configurations.

Responsibilities:
- Database Configuration
- Secret Key
- Upload Paths
- SQLAlchemy Settings
"""

import os


class Config:

    # =====================================================
    # Flask Secret Key
    # =====================================================
    SECRET_KEY = "your_secret_key_here"


    # =====================================================
    # JWT Configuration
    # =====================================================
    JWT_SECRET_KEY = "heritagehandcrafts_jwt_secret_key"

    JWT_ACCESS_TOKEN_EXPIRES = 86400


    # =====================================================
    # SQLite Database
    # =====================================================
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "heritage.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # =====================================================
    # Upload Folders
    # =====================================================
    PRODUCT_UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "products")

    ARTISAN_UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "artisan_profiles")

    GI_CERTIFICATE_FOLDER = os.path.join(BASE_DIR, "uploads", "gi_certificates")

    TEMP_UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "temp")


    # =====================================================
    # Allowed Image Extensions
    # =====================================================
    ALLOWED_IMAGE_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg",
        "webp"
    }


    # =====================================================
    # Allowed Video Extensions
    # =====================================================
    ALLOWED_VIDEO_EXTENSIONS = {
        "mp4",
        "mov",
        "avi"
    }


    # =====================================================
    # Maximum Upload Size
    # (50 MB)
    # =====================================================
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024