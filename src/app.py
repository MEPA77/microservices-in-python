from flask import Flask, jsonify, render_template, request
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(ip), str(hostname)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify({"mela": "pela"})

@app.route("/details")
def details():
    ip, hostname = fetchDetails()
    return render_template('index.html', hostname= hostname, ip = ip)

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5005)