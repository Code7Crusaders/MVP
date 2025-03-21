-- Inserimento utenti
INSERT INTO Users (username, password_hash, email, phone, first_name, last_name, is_admin) VALUES
('john_doe', 'hashed_password_1', 'john.doe@example.com', '1234567890123456', 'John', 'Doe', FALSE),
('admin_user', 'hashed_password_2', 'admin@example.com', '9876543210987654', 'Admin', 'User', TRUE),
('jane_smith', 'hashed_password_3', 'jane.smith@example.com', '1122334455667788', 'Jane', 'Smith', FALSE),
('michael_brown', 'hashed_password_4', 'michael.brown@example.com', '2233445566778899', 'Michael', 'Brown', FALSE);

-- Inserimento conversazioni
INSERT INTO Conversations (title) VALUES
('General Chat'),
('Support Discussion'),
('Development Talks'),
('Casual Conversations');

-- Inserimento messaggi
INSERT INTO Messages (text, user_id, conversation_id, rating, is_bot) VALUES
('Hello, how can I help you?', NULL, 1, NULL, TRUE),
('I have a problem with my account.', 1, 1, NULL, FALSE),
('What is the status of the latest deployment?', 2, 3, NULL, FALSE),
('The deployment is scheduled for tomorrow.', NULL, 3, NULL, TRUE),
('Does anyone know a good place to eat?', 3, 4, NULL, FALSE);

-- Inserimento ticket supporto
INSERT INTO Support (user_id, description, status, subject) VALUES
(1, 'My account is locked.', FALSE, 'Account Issue'),
(3, 'I cannot change my email address.', FALSE, 'Email Change Request'),
(4, 'The app crashes on startup.', TRUE, 'Bug Report');

-- Inserimento template
INSERT INTO Templates (question, answer, author, last_modified) VALUES
('How do I reset my password?', 'Go to settings and click on Reset Password.', 2, NOW()),
('What should I do if my account is locked?', 'Contact support to unlock your account.', 2, NOW()),
('How can I update my email address?', 'Go to profile settings and update your email.', 2, NOW());
