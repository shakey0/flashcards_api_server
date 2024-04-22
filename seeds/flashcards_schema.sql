DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS flashcard_sets CASCADE;
DROP SEQUENCE IF EXISTS flashcard_sets_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    oauth_provider TEXT,
    oauth_id TEXT,
    magic_link_token TEXT,
    magic_link_expiry TIMESTAMP,
    refresh_token TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT
);

CREATE TABLE flashcard_sets (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    emoji TEXT NOT NULL,
    previous_score INTEGER DEFAULT 0,
    theme_color TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    flashcards JSONB
);
