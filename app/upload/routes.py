from pathlib import Path
from flask import render_template, request, current_app
from app.upload import bp


@bp.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.files['video']:
            return render_template('upload.html')

        video_file = request.files['video']
        # TODO: add file type checking before saving
        video_file.save(str(Path(current_app.config['UPLOAD_FOLDER'], video_file.filename)))
        return render_template('upload_success.html', video_file=video_file)

    return render_template('upload.html')
