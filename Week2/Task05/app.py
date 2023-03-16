from flask import Flask, request, render_template, redirect, url_for
import datetime

import os

app = Flask(__name__)

# creates a root route, by default this room name is 'general'
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<room>")
def room(room):
    return render_template("index.html")

@app.route("/chat/<room>")
def get_chat_solo(room):
    with open('rooms/' + room + ".txt", "r") as file:
        chat = file.read()
    return chat, {"Content-Type":"text/plain"}

@app.route("/api/chat/<room>")
def get_chat(room):
    if not os.path.exists('rooms/' + room + ".txt"):
        os.mknod('rooms/' + room + ".txt")
    with open('rooms/' + room + ".txt", "r") as file:
        chat = file.read()
    return chat ,{"Content-Type":"text/plain"}

@app.route("/api/chat/<room>", methods=["POST"])
def post_chat(room):
    user = request.form["username"]
    message = request.form["msg"]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('rooms/' + room + ".txt", "a+") as file:
        file.write(f'{timestamp} {user}: {message}\n')
    return redirect(url_for("get_chat", room=room))

if __name__ == "__main__":
    app.run(host="0.0.0.0")