from flask import Flask

app = Flask(__name__)

def home():
  return render("login.html")

if __name__ == "__main__":
app.run(debug=True)