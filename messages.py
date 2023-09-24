from sqlalchemy.sql import text
from db import db
import users
False
def get_list_all():
    sql = text("SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_list():
    topic = users.topic_id()
    sql = text("SELECT M.content, U.username, T.topic, M.sent_at FROM messages M JOIN users U ON M.user_id = U.id JOIN topics T on M.topic = T.topic WHERE T.topic =:topic_name ORDER BY M.id;")
    result = db.session.execute(sql, {"topic_name": topic})
    return result.fetchall()

def send(content):
    user_id = users.user_id()
    topic = users.topic_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, topic, sent_at) VALUES (:content, :user_id, :topic, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id, "topic":topic})
    db.session.commit()
    return True
