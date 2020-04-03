from flask import Flask,render_template,redirect,request,url_for,session,flash
import os
import feedbackDB

app = Flask(__name__, static_url_path='')
app.secret_key = 'this is a secret key'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    post = feedbackDB.getFeedbacks()
    return render_template("index.html", post=post)

@app.route('/feedback')
def feedback():
    return render_template("fb.html")

@app.route('/feedback/send', methods=["POST","GET"])
def sendFeedback():
    name = request.form.get("name")
    msg = request.form.get("message")
    feedbackDB.createFeedback(name,msg)
    flash("Thanks for your feedback!","success")
    return redirect(url_for('feedback'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)


