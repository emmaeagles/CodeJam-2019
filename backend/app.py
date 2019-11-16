import os
from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS
from image_search import reverse_image_search
from object_detection import detect_objects
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./images"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def get_product_link():
    if "file" not in request.files:
        abort(400, "No file sent in request!")

    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    file_path = "./images/{}".format(filename)
    # detect all objects in original image
    # returns a tuple: (OBJECT, FILE_PATH)
    detected_objects = detect_objects(file_path)

    links = []
    # do a reverse image search on each detected object
    for object_tuple in detected_objects:
        link = reverse_image_search(object_tuple[1])
        links.append({"metadata": object_tuple[0], "link": link})

        # delete file after we're done with it
        os.remove(object_tuple[1])

    return jsonify(links)


if __name__ == "__main__":
    app.run(debug=True)
