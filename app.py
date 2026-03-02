from flask import Flask, render_template, request, send_file
from rembg import remove, new_session
import io
import uuid

app = Flask(__name__)

# 🔥 Usa modelo leve (evita estouro de memória)
session = new_session("u2netp")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")

        if file:
            input_bytes = file.read()

            output_bytes = remove(input_bytes, session=session)

            return send_file(
                io.BytesIO(output_bytes),
                mimetype="image/png",
                as_attachment=True,
                download_name=f"no-bg-{uuid.uuid4()}.png"
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)