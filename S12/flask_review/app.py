from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.values['uname']
        return render_template('login.html', name=name)



app.run()



