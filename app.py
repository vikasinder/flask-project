from flask import Flask, render_template, request, json, flash


app = Flask(__name__)


@app.route('/')  # http://127.0.0.1:5000/
def home():
    cr = "2021 Flask FrameWork Project By: - Vikas Sharma"
    return render_template('index.html')

# to embed python code in html we use jinja technique


@app.route('/aboutus')  # http://127.0.0.1:5000/about_us
def aboutus():
    return render_template('aboutus.html')


@app.route('/services')  # http://127.0.0.1:5000/about_us
def services():
    return render_template('services.html')


@app.route('/contact')  # http://127.0.0.1:5000/services
def contact():
    return render_template('contact.html')
