from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello There...</h1>'

@app.route("/extra")
def extra():
    return '<h1>Extra Page<h2>'


if __name__ == '__main__':
    app.run()
