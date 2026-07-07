from flask import Flask, jsonify, render_template
import packet_capture

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_capture", methods=["POST"])
def start():
    packet_capture.start_capture()
    return jsonify({"status": "started"})

@app.route("/stop_capture", methods=["POST"])
def stop():
    packet_capture.stop_capture()
    return jsonify({"status": "stopped"})

@app.route("/get_packets")
def get_packets():
    return jsonify(packet_capture.get_packets())

if __name__ == "__main__":
    app.run(debug=True, port=8080)