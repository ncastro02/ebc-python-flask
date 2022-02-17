from flask import Flask

app = Flask(__name__)

#si tu ni le dices a route que tipo de metodo http va usar, por default usará un GET
@app.route("/")
def Index():
  return "<a href='#'>hello world flask</a>"

@app.route("/ebc")
def HolaEBC():
  return "Hola ebc"

@app.route("/ebc/random")
def UnGetRandom():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(port=5000, debug=True)