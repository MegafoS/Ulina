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
    sql = text("SELECT M.content, U.username, T.topic, M.sent_at, U.id, M.id FROM messages M JOIN users U ON M.user_id = U.id JOIN topics T on M.topic = T.topic WHERE T.topic =:topic_name AND M.thread_id is NULL ORDER BY M.id DESC;")
    result = db.session.execute(sql, {"topic_name": topic})
    return result.fetchall()

def get_reply_list():
    topic = users.topic_id()
    sql = text("SELECT M.content, U.username, T.topic, M.sent_at, U.id, M.id, M.thread_id FROM messages M JOIN users U ON M.user_id = U.id JOIN topics T on M.topic = T.topic WHERE T.topic =:topic_name AND M.thread_id is not NULL ORDER BY M.id;")
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

def reply_send(content, thread_id):
    user_id = users.user_id()
    topic = users.topic_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, topic, sent_at, thread_id) VALUES (:content, :user_id, :topic, NOW(), :thread_id)")
    db.session.execute(sql, {"content":content, "user_id":user_id, "topic":topic, "thread_id":thread_id})
    db.session.commit()
    return True

def get_search_list(user_search, content_search):
        result = []
        if len(content_search)>0 and len(user_search)>0:
            sql = text("SELECT M.content, U.username, M.topic, M.sent_at, M.id FROM messages M JOIN users U ON M.user_id = U.id WHERE M.content LIKE :content_search AND U.username LIKE :user_search ORDER BY M.id DESC")
            result = db.session.execute(sql, {"content_search": f"%{content_search}%", "user_search": f"%{user_search}"})
        if len(user_search)>0 and len(content_search)==0:
            sql = text("SELECT M.content, U.username, M.topic, M.sent_at, M.id FROM messages M JOIN users U ON M.user_id = U.id WHERE U.username LIKE :user_search ORDER BY M.id DESC")
            result = db.session.execute(sql, {"user_search": f"%{user_search}"})
        if len(user_search)==0 and len(content_search)>0:
            sql = text("SELECT M.content, U.username, M.topic, M.sent_at, M.id FROM messages M JOIN users U ON M.user_id = U.id WHERE M.content LIKE :content_search ORDER BY M.id DESC")
            result = db.session.execute(sql, {"content_search": f"%{content_search}%"})
        return result

def delete_and_archive_message(message_id):
    sql = text("INSERT INTO deleted_messages (original_id, content, user_id, topic, sent_at, thread_id) SELECT id, content, user_id, topic, sent_at, thread_id FROM messages WHERE id = :message_id")
    db.session.execute(sql, {"message_id":message_id})
    db.session.commit()
    sql = text("DELETE FROM messages WHERE id =:message_id")
    db.session.execute(sql, {"message_id":message_id})
    db.session.commit()
    return True

def get_votes_list():
    sql = text("SELECT message_id, COUNT(CASE WHEN liked_by IS NOT NULL THEN 1 ELSE NULL END) AS likes FROM votes GROUP BY message_id ORDER BY message_id")
    result = db.session.execute(sql)
    return result.fetchall()