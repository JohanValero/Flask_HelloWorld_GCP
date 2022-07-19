from datetime import datetime
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    currentDateAndTime = datetime.now()
    return "Hola mundo de Johan: " + currentDateAndTime.strftime("%H:%M:%S")

gPORT = os.getenv('PORT', default=None)
print("PORT: ", gPORT)

app.run(host='0.0.0.0', port=gPORT)
