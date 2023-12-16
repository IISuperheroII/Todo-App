from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "844ffa228dc5e597dcc8b45b9bdee9cb31b06dd2"
app.config["MONGO_URI"] = ""

from application import routes