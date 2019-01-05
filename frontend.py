#FRONT_END STUFF
#Run Flask FLASK_APP=frontend.py flask run
from flask import Flask, render_template,request
from app import getPrices

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == "POST":
        print("Posted!")
        form = request.form
        d = list(request.form.to_dict().values())[0]
        if len(d)==14:
            d = d[:3]+d[4:]
        print(d)
        x = getPrices(d)
        return render_template('success.html',data=x[0],title=x[1])


if __name__ == '__main__':
    app.run(use_reloader=True)
