from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Home page"""
    return "<h1>My name is Bao</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
