from flask import Flask, render_template
from models import Users
app = Flask(__name__)
users = Users()

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)