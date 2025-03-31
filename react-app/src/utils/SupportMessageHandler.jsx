import { fetchSupportMessages as fetchSupportMessagesAPI } from './api';

export const sendSupportRequest = async (formData) => {
    const response = await fetch('/api/support', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });

    return response;
};

export const fetchSupportMessages = async () => {
    try {
        const messages = await fetchSupportMessagesAPI();
        return messages;
    } catch (error) {
        console.error('Error in SupportMessageHandler while fetching support messages:', error);
        throw error;
    }
};