from flask import render_template
from app.upload import bp


@bp.route('/upload')
def index():
    return render_template("upload.html")
