from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando en Render para pruebas de flask"

if __name__ == "__main__":
    app.run()