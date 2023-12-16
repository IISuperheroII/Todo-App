from application import app
from flask import render_template, redirect, request, flash
from .forms import TodoForm

@app.route("/")
def index():
    return render_template("index.html", title="")
@app.route("/add_todo")
def add_todo():
    form = TodoForm()
    return render_template("add_todo.html", form = form)