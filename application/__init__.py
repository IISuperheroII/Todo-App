from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["SECRET_KEY"] = "844ffa228dc5e597dcc8b45b9bdee9cb31b06dd2"
app.config["MONGO_URI"] = "mongodb+srv://wael22ka:ANs8rcM0OVhVezsY@cluster0.gaad0pv.mongodb.net/MyFirstDatabase?retryWrites=true&w=majority"

try:
    mongodb_client = PyMongo(app)
    db = mongodb_client.db

    if db is None:
        print("Error: Could not connect to the database.")
    else:
        print("Connected to the database successfully.")
except Exception as e:
    print(f"Error: {e}")

from application import routes