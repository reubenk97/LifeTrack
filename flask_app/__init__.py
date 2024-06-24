from flask import Flask

app = Flask(__name__)
app.secret_key = "life is meant to be enjoyed"

DB = "LifeTrack"