from flask import Flask, jsonify ,render_template
import socket
app = Flask(__name__)

#   Function to fetch hostname and ip
def  fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")  
def health ():
    return jsonify(
        status="up"
    )  
@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

 