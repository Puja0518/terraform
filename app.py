
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return """<p>Hello, Shital !</p>
                Welcome to the CI/CD ! 

                New App Created!! Deployed now and beforeeeee
            """


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5050)