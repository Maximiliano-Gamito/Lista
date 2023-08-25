from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/links")
def links():
    return render_template("links.html")

if __name__ == "__main__":
    app.run(debug=True)
