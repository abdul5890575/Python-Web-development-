from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" \
            "<p>you can add tags </p>"

##<converter:variable>
@app.route("/user/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/temp")
def renderstaticfile():
    return render_template("examplefile.html")



if __name__== '__main__':
    app.run(debug=True)