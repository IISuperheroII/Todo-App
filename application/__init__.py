from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "844ffa228dc5e597dcc8b45b9bdee9cb31b06dd2"
app.config["MONGO_URI"] = "mongodb+srv://wael22ka:bdpcCdeVsPjQNdGX@cluster0.gaad0pv.mongodb.net/?retryWrites=true&w=majority"

#setuo PyMongo
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes