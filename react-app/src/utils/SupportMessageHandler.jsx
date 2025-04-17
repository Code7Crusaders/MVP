import { fetchSupportMessages as fetchSupportMessagesAPI, markSupportMessageDone as markSupportMessageDoneAPI } from './api';

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

export const markSupportMessageDone = async (supportMessageId) => {
    try {
        const result = await markSupportMessageDoneAPI(supportMessageId);
        return result;
    } catch (error) {
        console.error('Error in SupportMessageHandler while marking support message as done:', error);
        throw error;
    }
};

