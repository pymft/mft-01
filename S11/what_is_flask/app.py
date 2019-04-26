from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route("/user/<name>/<int:rep>")
def whatever(name=None, rep=1):
    return f"<h1>Hello {name}</h1>" * rep


@app.route('/table')
def table():
    return """<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>"""


app.run()

