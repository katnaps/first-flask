from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def index(name):
    name = name.upper()
    return render_template('index.html', name=name)

# @app.route("/extra")
# def extra():
#     return '<h1>Extra Page<h2>'

# @app.route("/user/<username>")
# def user(username):
#     return f"Hi {username}"


if __name__ == '__main__':
    app.run()
