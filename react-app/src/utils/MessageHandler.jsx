import { fetchMessages, saveMessage, chatInteract, updateMessageRating, saveConversationTitle ,deleteConversation } from './api';

// Fetch messages for a specific conversation
export const loadMessages = async (chatId) => {
    try {
        const data = await fetchMessages(chatId);

        // Map the rating field from the database to the selectedRating property
        return data.map((message) => ({
            ...message,
            selectedRating: message.rating, // Map the rating field to selectedRating
        }));
    } catch (error) {
        console.error('Error loading messages:', error);
        throw error;
    }
};

// Save a new message
export const saveNewMessage = async (messageData) => {
    try {
        const savedMessage = await saveMessage(messageData);
        return { ...messageData, id: savedMessage.id, created_at: new Date() };
    } catch (error) {
        console.error('Error saving message:', error);
        throw error;
    }
};

// Handle feedback for a message
export const handleFeedback = (messages, messageId, isPositive) => {
    return messages.map((message) =>
        message.id === messageId
            ? { ...message, selectedRating: isPositive } // Add or update the selectedRating property
            : message
    );
};

// Update the rating in the database
export const updateFeedback = async (messageId, isPositive) => {
    try {
        await updateMessageRating(messageId, isPositive);
    } catch (error) {
        console.error('Error updating message rating:', error);
        throw error;
    }
};


// Interact with the chat endpoint and save the bot's response
export const interactWithChat = async (inputValue, chatId) => {
    try {
        const botResponse = await chatInteract(inputValue);

        // Create the bot's message
        const botMessage = {
            text: botResponse.answer,
            conversation_id: chatId,
            rating: null,
            is_bot: true,
        };

        const savedBotMessage = await saveMessage(botMessage);
        return { ...botMessage, id: savedBotMessage.id, created_at: new Date() };
    } catch (error) {
        console.error('Error interacting with chat:', error);
        throw error;
    }
};

export const createChat = async (title) => {
    try {
        await saveConversationTitle( title );
    } catch (error) {
        console.error('Error creating chat:', error);
        throw error;
    }
}

export const deleteChat = async (chatID) => {
    try {
        await deleteConversation(chatID);
    } catch (error) {
        console.error('Error deleting chat:', error);
        throw error;
    }
}