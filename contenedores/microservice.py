from flask import Flask, jsonify

microservice = Flask(__name__)

@microservice.route("/")
def getRoot():
    return jsonify(
        status="OK",
    )

@microservice.route("/status")
def getStatus():
    return jsonify(
        status="OK",
    )

if __name__ == '__main__':
    microservice.run(debug=True,host='0.0.0.0')
