from app import app
from sqlalchemy.sql import text
from db import db
from flask import render_template, request, redirect
import messages, users

@app.route("/")
def index():
    list = messages.get_list_all()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/reply<int:message_id>", methods= ["GET", "POST"])
def reply_message(message_id):
    if request.method == "POST":
        content = request.form['content']
        topic = users.topic_id()
        thread_id = message_id
        if messages.reply_send(content, thread_id):
            return redirect(f'/{topic}')
        else:
            return render_template("error.html", message="Viestin lähetys ei onnistunut, tarkista oletko kirjautunut")
    return render_template('reply.html', message_id=message_id)

@app.route("/send", methods=["POST"])
def send():
    topic = users.session["current_topic"]
    content = request.form["content"]
    if messages.send(content):
        return redirect(f"/{topic}")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut, tarkista oletko kirjautunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/vapaa", methods=["GET"])
def topic_0():
    users.session["current_topic"]='vapaa'
    list = messages.get_list()
    replies_list = messages.get_reply_list()
    vote_list = messages.get_votes_list()
    if request.method == "GET":
        return render_template("topic_0.html", count=len(list)+len(replies_list), messages=list, replies = replies_list, votes = vote_list)
@app.route("/pelit", methods=["GET"])
def topic_1():
    users.session["current_topic"]='pelit'
    list = messages.get_list()
    replies_list = messages.get_reply_list()
    vote_list = messages.get_votes_list()
    if request.method == "GET":
        return render_template("topic_1.html", count=len(list)+len(replies_list), messages=list, replies = replies_list, votes = vote_list)
@app.route("/ruoka", methods=["GET"])
def topic_2():
    users.session["current_topic"]='ruoka'
    list = messages.get_list()
    replies_list = messages.get_reply_list()
    vote_list = messages.get_votes_list()
    if request.method == "GET":
        return render_template("topic_2.html", count=len(list)+len(replies_list), messages=list, replies = replies_list, votes = vote_list)
@app.route("/uutiset", methods=["GET"])
def topic_3():
    users.session["current_topic"]='uutiset'
    list = messages.get_list()
    replies_list = messages.get_reply_list()
    vote_list = messages.get_votes_list()
    if request.method == "GET":
        return render_template("topic_3.html", count=len(list)+len(replies_list), messages=list, replies = replies_list, votes = vote_list)
@app.route("/sarjat_ja_elokuvat", methods=["GET"])
def topic_4():
    users.session["current_topic"]='sarjat_ja_elokuvat'
    list = messages.get_list()
    replies_list = messages.get_reply_list()
    vote_list = messages.get_votes_list()
    if request.method == "GET":
        return render_template("topic_4.html", count=len(list)+len(replies_list), messages=list, replies = replies_list, votes = vote_list)
    
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        user_search = request.form["user_search"]
        content_search = request.form["content_search"]
        result = messages.get_search_list(user_search, content_search)
        return render_template("search.html", messages=result)
    else:
        return render_template("search.html", messages=[])
    
@app.route('/delete_message<int:message_id>', methods=["POST"])
def delete_message(message_id):
    user_id = users.user_id()
    if request.method == "POST" and user_id is not None:
        topic = users.topic_id()
        if messages.delete_and_archive_message(message_id):
            return redirect(f"/{topic}")
        else:
            return render_template("error.html", message="Viestin poistaminen ei onnistunut")

@app.route('/like_message/<int:message_id>')
def like_message(message_id):
    topic = users.topic_id()
    user_id = users.user_id()
    sql = text("DELETE FROM votes WHERE message_id=:message_id AND (liked_by=:user_id OR disliked_by=:user_id)")
    db.session.execute(sql, {"message_id":message_id, "user_id":user_id})
    db.session.commit()
    sql = text("INSERT INTO votes (message_id, liked_by) VALUES (:message_id, :user_id)")
    db.session.execute(sql, {"message_id":message_id, "user_id":user_id})
    db.session.commit()
    return redirect(f"/{topic}")

@app.route('/dislike_message/<int:message_id>')
def dislike_message(message_id):
    topic = users.topic_id()
    user_id = users.user_id()
    sql = text("DELETE FROM votes WHERE message_id=:message_id AND (liked_by=:user_id OR disliked_by=:user_id)")
    db.session.execute(sql, {"message_id":message_id, "user_id":user_id})
    db.session.commit()
    sql = text("INSERT INTO votes (message_id, disliked_by) VALUES (:message_id, :user_id)")
    db.session.execute(sql, {"message_id":message_id, "user_id":user_id})
    db.session.commit()
    return redirect(f"/{topic}")
