// Fetch all messages for a specific conversation
export const fetchMessages = async (chatId) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch(`http://127.0.0.1:5000/message/get_by_conversation/${chatId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch messages');
    }

    const data = await response.json();
    console.log('Fetched messages:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error fetching messages:', error);
    throw error;
  }
};

// Save a new message to the database
export const saveMessage = async (messageData) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch('http://127.0.0.1:5000/message/save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(messageData),
    });

    if (!response.ok) {
      throw new Error('Failed to save message');
    }

    const data = await response.json();
    console.log('Message saved:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error saving message:', error);
    throw error;
  }
};

// Fetch all conversations
export const fetchConversations = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch('http://127.0.0.1:5000/conversation/get_all', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch conversations');
    }

    const data = await response.json();
    console.log('Fetched conversations:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error fetching conversations:', error);
    throw error;
  }
};