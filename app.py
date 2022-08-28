from datetime import datetime
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    currentDateAndTime = datetime.now()
    vStringData = "Hola mundo de " + str(gAUTHOR_NAME) + " in port [" + str(gPORT) + "]: " + currentDateAndTime.strftime("%H:%M:%S")
    return vStringData

gPORT = os.getenv('PORT', default=None)
gAUTHOR_NAME = os.getenv("AUTHOR", default=None)
print("PORT: ", gPORT)

app.run(host='0.0.0.0', port=gPORT)
