from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    currentDateAndTime = datetime.now()
    return "Hola mundo: " + currentDateAndTime.strftime("%H:%M:%S")

app.run(host='0.0.0.0', port=81)