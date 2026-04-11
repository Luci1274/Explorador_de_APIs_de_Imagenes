from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route("/")
def index():
    return "hola mundo"

if __name__ == "__main__":
    app.run(debug=True)