# Libraraies are imported that are used in this project
from flask import Flask, render_template, json , request , flash
import os

if(os.path.exists("env.py")):
    import env

app = Flask(__name__)

app.secret_key=os.environ.get("SECRET_KEY")

# context processor is used here -- for passing Dictonary value on all the pages 
@app.context_processor
def utility_processor():
    data=[]
    with open("data/yoga.json") as yoga_json:
        data=json.load(yoga_json)
        # Returning Dictonary
    return dict(values=data)

# context processor is used here -- for passing Dictonary value on all the pages 
@app.context_processor
def utility_processor():
    data1=[]
    with open("data/yoga_details.json") as y_json:
        data1=json.load(y_json)
    return dict(details=data1)

@app.route('/')  
def home():
    return render_template('index.html')


@app.route('/aboutus')  
def aboutus():
    return render_template('aboutus.html')

# dynamically passing class_yoga values
@app.route('/base/<class_yoga>')  
def about_yoga(class_yoga):
    yoga={}
    with open("data/yoga.json") as yoga_json:
        data=json.load(yoga_json)
        for val in data:
            if val["url"] == class_yoga:
                yoga=val
    return render_template('yoga.html', yoga_value=yoga)

@app.route('/services')  
def services():
   
    return render_template('services.html')


@app.route('/services/<yoga_details>')  
def details(yoga_details):
    y_details={}
    with open("data/yoga_details.json") as details_json:
        data=json.load(details_json)
        for value in data:
            if value["url"] == yoga_details:
                    y_details=value
        return render_template('yoga_details.html', details_yoga=y_details)

# form get/post method
@app.route('/contact',methods=["GET","POST"])  
def contact():
    if request.method=="POST":
        flash("Thanks  {} , We Have Receieved Your Message, Will Contact You Soon ".format(request.form.get("name")))
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)
