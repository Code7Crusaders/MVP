
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

-- Creazione della tabella User_Messages
CREATE TABLE User_Messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    conversation_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (conversation_id) REFERENCES Conversations(id) ON DELETE CASCADE
);

-- Creazione della tabella Bot_Messages
CREATE TABLE Bot_Messages (
    id SERIAL PRIMARY KEY,
    text VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating BOOLEAN,
    conversation_id INTEGER NOT NULL,
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
    author VARCHAR NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author) REFERENCES Users(username) ON DELETE CASCADE
);

-- Creazione della tabella Products
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    country_of_origin VARCHAR NOT NULL,
    weight INTEGER,
    milk_type VARCHAR,
    description VARCHAR,
    manufacturer VARCHAR,
    product_name VARCHAR NOT NULL,
    image BYTEA
);

-- Creazione della tabella Message_Products (relazione molti-a-molti tra messaggi e prodotti)
CREATE TABLE Message_Products (
    message_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    PRIMARY KEY (message_id, product_id),
    FOREIGN KEY (message_id) REFERENCES User_Messages(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
);
