from flask import Flask, request, jsonify
from http import HTTPStatus


import serial, datetime
from db import store_temp

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'message': 'OK'}), HTTPStatus.OK

@app.route("/post_temp", methods=['POST'])
def post_temp():
    json_ = request.json
    data = json_['data']

    param = 'Temperature'
    reading = data
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    store_temp(param, reading, created_at)

    with open('temperature_data.txt', 'a+') as f:
        f.write(f"\ntimestamp: {created_at}\nreading: {reading}\n")

    return jsonify({'message': 'OK'}), HTTPStatus.OK
