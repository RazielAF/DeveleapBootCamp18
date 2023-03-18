from flask import Flask,render_template,request,url_for,redirect
import datetime
import os

app = Flask(__name__)
date_create = datetime.datetime.now().strftime("%Y-%m-%d")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<room>")
def room(room):
    return render_template("index.html")

@app.route("/chat/<room>")
def get_chat(room):
    try:
        filename = os.path.join("ChatroomsLogs", f"{room}.{date_create}.txt")
        if not os.path.isfile(filename):
            return "No Such Room"
        with open(filename,"r") as file:
            chat = file.read()
        return chat, {"Content-Type": "text/plain"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/api/chat/<room>")
def get_single_chat(room):
    filename = os.path.join("ChatroomsLogs", f"{room}.{date_create}.txt")
    if not os.path.exists(filename):
           os.mknod(filename)
    with open(filename,"r") as file:
        chat = file.read()
    return chat, {"Content-Type": "text/plain"}

@app.route("/api/chat/<room>", methods=["POST"])
def post_chat(room):
    try:
        user = request.form["username"]
        message = request.form["msg"]
    except KeyError:
        return {"error": "Missing username or message field in request"}, 400
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = os.path.join("ChatroomsLogs", f"{room}.{date_create}.txt")
    with open(filename, "a+") as file:
        file.write(f"{date} {user}: {message}\n")
    return redirect(url_for("get_single_chat", room=room))

if __name__ == "__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')
