from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Deployment successful via Github Actions and Ansible1"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
