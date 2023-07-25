import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    UPLOAD_FOLDER = "uploads"
    ALLOWED_EXTENSIONS = {'mp4', 'mov'}
