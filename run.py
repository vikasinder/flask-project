from flask import Flask, render_template, json , request , flash
import os

if(os.path.exists("env.py")):
    import env

app = Flask(__name__)

app.secret_key=os.environ.get("SECRET_KEY")

@app.context_processor
def utility_processor():
    data=[]
    with open("data/yoga.json") as yoga_json:
        data=json.load(yoga_json)
    return dict(values=data)


@app.route('/')  # http://127.0.0.1:5000/
def home():
    # data=[]
    # with open("data/yoga.json") as yoga_json:
    #     data=json.load(yoga_json)
   
    return render_template('index.html' )

# to embed python code in html we use jinja technique


@app.route('/aboutus')  # http://127.0.0.1:5000/about_us
def aboutus():
    return render_template('aboutus.html')


@app.route('/base/<class_yoga>')  # http://127.0.0.1:5000/about_us
def about_yoga(class_yoga):
    yoga={}
    with open("data/yoga.json") as yoga_json:
        data=json.load(yoga_json)
        for val in data:
            if val["url"] == class_yoga:
                yoga=val
    return render_template('yoga.html', yoga_value=yoga)

@app.route('/services')  # http://127.0.0.1:5000/about_us
def services():
   
    return render_template('services.html')


@app.route('/contact',methods=["GET","POST"])  # http://127.0.0.1:5000/services
def contact():
    if request.method=="POST":
        
        flash("Thanks  {} , We Have Receieved Your Message, Will Contact You Soon ".format(request.form.get("name")))
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
