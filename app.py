from flask import Flask
app = Flask(__name__)

@app.route('/epl')
def hello_world():
    return 'Hello, World of epl goda boda voda!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True, debug=True)
