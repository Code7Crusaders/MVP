-- Creazione della tabella Users
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256) NOT NULL UNIQUE,
    password_hash VARCHAR(512) NOT NULL,
    email VARCHAR(256) NOT NULL UNIQUE,
    phone CHAR(16),
    first_name VARCHAR(256) NOT NULL,
    last_name VARCHAR(256) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Creazione della tabella Conversations
CREATE TABLE Conversations (
    id SERIAL PRIMARY KEY,
    title VARCHAR(256) NOT NULL
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Creazione della tabella Messages
CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    conversation_id INTEGER NOT NULL,
    rating BOOLEAN,
    is_bot BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
);

-- Creazione della tabella Support
CREATE TABLE Support (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description VARCHAR(1024) NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    subject VARCHAR(256) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Creazione della tabella Templates
CREATE TABLE Templates (
    id SERIAL PRIMARY KEY,
    question VARCHAR(1024) NOT NULL,
    answer VARCHAR(1024) NOT NULL,
    author INTEGER NOT NULL,
    last_modified TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author) REFERENCES Users(id) ON DELETE CASCADE
);

-- Query to delete the Templates table and all rows in all tables
-- DROP TABLE IF EXISTS Templates CASCADE;
-- DROP TABLE IF EXISTS Support CASCADE;
-- DROP TABLE IF EXISTS Messages CASCADE;
-- DROP TABLE IF EXISTS Conversations CASCADE;
-- DROP TABLE IF EXISTS Users CASCADE;