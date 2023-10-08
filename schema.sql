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
