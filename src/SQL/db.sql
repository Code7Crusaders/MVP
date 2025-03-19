-- Creazione della tabella Users
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256) NOT NULL UNIQUE,
    password_hash VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone CHAR(16),
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Creazione della tabella Conversations
CREATE TABLE Conversations (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL
);

-- Creazione della tabella Messages
CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    conversation_id INTEGER NOT NULL,
    rating BOOLEAN,
    is_bot BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
);


-- Creazione della tabella Support
CREATE TABLE Support (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description VARCHAR NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    subject VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Creazione della tabella Templates
CREATE TABLE Templates (
    id SERIAL PRIMARY KEY,
    question VARCHAR NOT NULL,
    answer VARCHAR NOT NULL,
    author SERIAL NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author) REFERENCES Users(id) ON DELETE CASCADE
);

-- Query to delete the Templates table and all rows in all tables
-- DROP TABLE IF EXISTS Templates CASCADE;
-- DROP TABLE IF EXISTS Support CASCADE;
-- DROP TABLE IF EXISTS Messages CASCADE;
-- DROP TABLE IF EXISTS Conversations CASCADE;
-- DROP TABLE IF EXISTS Users CASCADE;