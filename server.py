from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def about():
    return render_template("index.html")


@app.route('/submit_form', methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)

    return "form_submitted"
