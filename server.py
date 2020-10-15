from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route("/")
# def index():
#     signed_in = True
#     return render_template('index.html', signed_in=signed_in)

@app.route("/")
def index():
    first_name = request.args.get('first_name')
    return render_template('index.html', first_name=first_name)

@app.route("/contact")
def contact():
    return render_template('contact.html')

# @app.route("/<name>")
# def index(name):
#     name = name.upper()
#     return render_template('index.html', name=name)

# @app.route("/extra")
# def extra():
#     return '<h1>Extra Page<h2>'

# @app.route("/user/<username>")
# def user(username):
#     return f"Hi {username}"


if __name__ == '__main__':
    app.run()
