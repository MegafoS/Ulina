CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    topic TEXT,
    sent_at TIMESTAMP,
    thread_id INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic TEXT
);
INSERT INTO topics (id, topic) VALUES (0, 'vapaa'), (1, 'pelit'), (2, 'ruoka'), (3, 'uutiset'), (4, 'sarjat_ja_elokuvat');

CREATE TABLE deleted_messages (
    id SERIAL PRIMARY KEY,
    original_id INTEGER,
    content TEXT,
    user_id INTEGER REFERENCES users,
    topic TEXT,
    sent_at TIMESTAMP,
    thread_id INTEGER
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER,
    liked_by INTEGER,
    disliked_by INTEGER
);
