from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

def get_temperature_data():
    uv = random.randint(1, 10)
    precipitation = random.randint(0, 100)
    humidity = random.randint(30, 80)
    pm25 = round(random.uniform(0.1, 50.0), 2)
    time.sleep(0.1)
    return {
        "uv": uv,
        "precipitation": precipitation,
        "humidity": humidity,
        "pm25": pm25,
    }

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['GET'])
def temperature():
    temperature_data = get_temperature_data()
    return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(debug=True)
