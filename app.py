from flask import Flask, render_template, request
from database import add_user_to_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/signup", methods=['post'])
def sign_up():
    data = request.form
    # store in db and display acknowledgement
    add_user_to_db(data)
    return render_template('signup_success.html', name=data['firstName'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)