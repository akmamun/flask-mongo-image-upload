from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import db as d

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/training/face/', methods=['GET'])
def face_upload_file():
    return render_template('upload.html')


@app.route('/training/face/upload', methods=['POST'])
def face_upload():
    target = os.path.join(APP_ROOT, 'face-images/')  #folder path
    if not os.path.isdir(target):
            os.mkdir(target)     # create folder if not exits
    face_db_table = d.mongo.db.faces  # database table name
    if request.method == 'POST':
        for upload in request.files.getlist("face_image"): #multiple image handel
            filename = secure_filename(upload.filename)
            destination = "/".join([target, filename])
            upload.save(destination)
            face_db_table.insert({'face_image': filename})   #insert into database mongo db

        return 'Image Upload Successfully'


if __name__ == '__main__':
    app.run()
