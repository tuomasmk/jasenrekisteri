from flask import Flask, render_template
app = Flask(__name__)

class Item:
	def __init__(self, name):
		self.name = name

nimi = "Mikki Hiiri"

lista = [1, 1, 2, 3, 5, 8, 13]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Viides"))
esineet.append(Item("Neljäs"))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
	return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

if __name__ == "__main__":
    app.run(debug=True)
