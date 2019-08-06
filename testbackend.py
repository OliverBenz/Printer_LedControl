from flask import Flask, request, jsonify
import json

app = Flask(__name__)

httpHeaders = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
}

@app.route('/api/job', methods=['GET'])
def getTest():
    result = {
        "job": {
            "averagePrintTime": 38923.424780887, 
            "estimatedPrintTime": 33079.77878218678, 
            "filament": {
            "tool0": {
                "length": 30124.544599997087, 
                "volume": 0.0
            }
            }, 
            "file": {
            "date": 1563137072, 
            "display": "nespresso-holder_10h5min_30,09_90_1,97.gcode", 
            "name": "nespresso-holder_10h5min_30-09_90_1-97.gcode", 
            "origin": "local", 
            "path": "Queue/nespresso-holder_10h5min_30-09_90_1-97.gcode", 
            "size": 8960200
            }, 
            "lastPrintTime": 38923.424780887, 
            "user": "OliverBenz"
        }, 
        "progress": {
            "completion": 100.0, 
            "filepos": 8960200, 
            "printTime": 38923, 
            "printTimeLeft": 0, 
            "printTimeLeftOrigin": 0
        }, 
        "state": "Operational"
    }

    return jsonify(result), 200, httpHeaders

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3004)