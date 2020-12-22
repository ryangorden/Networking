from flask import Flask,requests, jsonify

app- Flask(__name__)


@app.route('/index')
def index():
    pass


@app.route('/login')
def login():
    pass

@app.route('/auth')
def auth():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
