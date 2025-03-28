import './api.jsx'

// Delete a new message
export const deleteConversation = async (conversationId) => {
    try {
        const response = await deleteConversationAPI(conversationId); // Assuming deleteConversationAPI is defined in './api.jsx'
        return response;
    } catch (error) {
        console.error('Error deleting conversation:', error);
        throw error;
    }
};