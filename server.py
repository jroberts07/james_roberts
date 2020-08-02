import os
import json
from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config["MAIL_USE_TLS"] = True,
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_PASSWORD")
mail = Mail(app)


@app.route('/')
def about():
    return render_template("index.html")


@app.route('/submit_form', methods=["POST"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        msg = Message(
            body=json.dumps(data),
            subject="Website request",
            sender=os.environ.get("EMAIL"),
            recipients=[os.environ.get("EMAIL")]
        )
        mail.send(msg)
        return render_template("index.html")

