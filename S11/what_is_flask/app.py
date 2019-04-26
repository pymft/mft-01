from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user/<name>/<int:rep>")
def whatever(name=None, rep=1):
    return f"<h1>Hello {name}</h1>" * rep


@app.route('/table/<int:m>/<int:n>')
def table(m=1, n=1 ):
    column = "<tr> " + "<td> whatever </td>" * n + "</tr>"
    inside_text = column * m
    return f"""<table style="width:100%">{inside_text}</table>"""


app.run()
