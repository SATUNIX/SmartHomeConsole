from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
import random
import time
@app.route('/controllers', methods=['GET','POST'])
@app.route('/controllers.html', methods=['GET', 'POST'])
def content_manager():
    return render_template('controllers.html')

# Importing the external controller library
import controller_library

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/back_light_on')
def BackLightOn():
    controller_library.BackLight.on()
    return redirect(url_for('index'))

@app.route('/back_light_off')
def BackLightOff():
    controller_library.BackLight.off()
    return redirect(url_for('index'))

@app.route('/top_light_on')
def TopLightOn():
    controller_library.TopLight.on()
    return redirect(url_for('index'))

@app.route('/top_light_off')
def TopLightOff():
    controller_library.TopLight.off()
    return redirect(url_for('index'))

@app.route('/fountain_on')
def FountainOn():
    controller_library.Fountain.on()
    return redirect(url_for('index'))

@app.route('/fountain_off')
def FountainOff():
    controller_library.Fountain.off()
    return redirect(url_for('index'))

@app.route('/plants_on')
def PlantsOn():
    controller_library.Plants.on()
    return redirect(url_for('index'))

@app.route('/plants_off')
def PlantsOff():
    controller_library.Plants.off()
    return redirect(url_for('index'))

'''
JAVASCRIPT DATA STREAM ROUTE
'''
def get_temperature_data():
    uv = random.randint(1, 10)
    precipitation = random.randint(0, 100)
    humidity = random.randint(30, 80)
    pm25 = round(random.uniform(0.1, 50.0), 2)
    time.sleep(1)
    return {
        "uv": uv,
        "precipitation": precipitation,
        "humidity": humidity,
        "pm25": pm25,
        "temperature":temperature,
    }
@app.route('/alldata', methods=['GET'])
def temperature():
    temperature_data = get_temperature_data()
    return jsonify(alldata)

#INDEX ROUTE
@app.route('/', methods=['GET'])
@app.route('/home.html', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/upload.html', methods=['POST', 'GET'])
def upload_file():
    if 'file-upload' not in request.files:
        return render_template('upload.html')
    uploaded_file = request.files['file-upload']
    if uploaded_file.filename == '':
        return render_template('upload.html')

    mime_type = mimetypes.guess_type(uploaded_file.filename)[0]
    # Check if the file is an image (jpeg or png)
    if mime_type not in ['image/jpeg', 'image/png']:
        return "Invalid file type. Please upload a JPEG or PNG image.", 400
    filename = secure_filename(uploaded_file.filename)
    try:
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except Exception as e:
        print("Exception occurred:", e)
        return "File either already exists or is not a JPEG or PNG image type.", 400
    return redirect(url_for('content_manager'))  # Redirect to contentmanager.html


@app.route('/Contact-Us.html', methods=['GET'])
@app.route('/Contact-Us', methods=['GET'])

def contact_us():
    return render_template('Contact-Us.html')

@app.route('/controllers.html', methods=['GET'])
@app.route('/controllers', methods=['GET'])
def information():
    return render_template('controllers.html')


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=8088, debug=False)

