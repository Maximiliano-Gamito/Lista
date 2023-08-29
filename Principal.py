from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/resumo")
def resumo():
    return render_template("resumo.html")
@app.route("/links")
def links():
    return render_template("links.html")
@app.route("/planilha")
def planilha():
    return render_template("planilha.html")
@app.route("/renomeador")
def renomeador():
    return render_template("renomeador.html")
@app.route("/legado")
def legado():
    return render_template("legado.html")
@app.route("/normativos")
def normativos():
    return render_template("normativos.html")
@app.route("/sicaq")
def sicaq():
    return render_template("sicaq.html")
@app.route("/site")
def site():
    return render_template("site.html")
@app.route("/teto")
def teto():
    return render_template("teto.html")
@app.route("/limitrofes")
def limitrofes():
    return render_template("limitrofes.html")

if __name__ == "__main__":
    app.run(debug=True)
