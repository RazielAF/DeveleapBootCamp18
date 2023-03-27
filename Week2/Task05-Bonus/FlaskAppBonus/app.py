
from flask import Flask, render_template, request, url_for, redirect
import datetime
import mysql.connector
from mysql.connector import pooling
import logging
import socket

app = Flask(__name__)
date_create = datetime.datetime.now().strftime("%Y-%m-%d")

db = mysql.connector.connect(
    host='db',
    user='root',
    password='password',
    database='chatlogs'
)

pool =pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=3,
    host='db',
    user='root',
    password='password',
    database='chatlogs'
)
# Get the container IP address(for load balancing)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<room>")
def room(room):
    return render_template("index.html")

#getting data from the sql data base based on the given room 
@app.route("/chat/<room>")
def get_chat(room):
    try:
        conn=pool.get_connection()
        with db.cursor() as cur:#cursor will be closed after finishing,preventing resource leaks
            cur.execute("SELECT logged, username, messages FROM chat WHERE room = %s", (room,))
            chat = cur.fetchall()
            formatted_chat = [f"[{msg[0]}] {msg[1]}: {msg[2]}<br/>\n" for msg in chat]
            conn.close()
        return f'\n' + "\n".join(formatted_chat)
    except Exception as e:
        logging.exception("An error occurred while getting chat data") 
        return {"error": "An error occurred while getting chat data"}, 500

#getting data from the sql data base based on the given room 
#Show the data with the form

@app.route("/api/chat/<room>")
def get_single_chat(room):
    conn=pool.get_connection()
    with db.cursor() as cur:
        cur.execute("SELECT logged, username, messages FROM chat WHERE room = %s LIMIT 100", (room,))
        messages = [f"[{msg[0]}] {msg[1]}: {msg[2]}"  for msg in cur.fetchall()]
        conn.close()
    return f'{ip_address}\n'+"\n".join(messages)

#Getting data from user and inserting into the Mysql DB

@app.route("/api/chat/<room>", methods=["POST"])
def post_chat(room):
    try:
        conn=pool.get_connection()
        user = request.form.get("username", "").strip()#Removing white spaces
        message = request.form.get("msg", "").strip()
        if not user or not message: #checking if both fields provided
            return {"error": "Username or message field is empty"}, 400
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with db.cursor() as cur:#cursor will be closed after finishing,preventing resource leaks
            cur.execute(
                "INSERT INTO chat (room, logged, username, messages) VALUES (%s, %s, %s, %s)",
                (room, str(date), user, message),
            )
            db.commit()
            conn.close()
        return redirect(url_for("get_single_chat", room=room))
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
