from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            filename = str(uuid.uuid4()) + ".png"
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            output_path = os.path.join(UPLOAD_FOLDER, "no-bg-" + filename)

            file.save(input_path)

            with open(input_path, "rb") as i:
                input_data = i.read()
                output_data = remove(input_data)

            with open(output_path, "wb") as o:
                o.write(output_data)

            return render_template("index.html", download_file=output_path)

    return render_template("index.html", download_file=None)


@app.route("/download")
def download():
    file_path = request.args.get("file")
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)