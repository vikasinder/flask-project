from flask import Flask, render_template, json
import os

app = Flask(__name__)


@app.route('/')  # http://127.0.0.1:5000/
def home():
   
    return render_template('index.html' )

# to embed python code in html we use jinja technique


@app.route('/aboutus')  # http://127.0.0.1:5000/about_us
def aboutus():
    return render_template('aboutus.html')


@app.route('/services')  # http://127.0.0.1:5000/about_us
def services():
    data=[]
    with open("data/yoga.json") as yoga_json:
        data=json.load(yoga_json)
    return render_template('services.html',values=data)


@app.route('/contact')  # http://127.0.0.1:5000/services
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
