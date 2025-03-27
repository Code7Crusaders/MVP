// Fetch all messages for a specific conversation
export const fetchMessages = async (chatId) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch(`http://127.0.0.1:5001/message/get_by_conversation/${chatId}`, {
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

  if (!token) {
    console.error('Error: No token found in localStorage');
    throw new Error('Authentication token is missing');
  }

  if (!messageData || typeof messageData !== 'object') {
    console.error('Error: Invalid message data provided', messageData);
    throw new Error('Invalid message data');
  }

  try {
    const response = await fetch('http://127.0.0.1:5001/message/save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(messageData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Error response from server:', errorData);
      throw new Error(errorData.error || 'Failed to save message');
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
    const response = await fetch('http://127.0.0.1:5001/conversation/get_all', {
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

// Interact with the chat endpoint
export const chatInteract = async (question) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch('http://127.0.0.1:5001/api/chat_interact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to interact with chat');
    }

    const data = await response.json();
    console.log('Chat interaction response:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error interacting with chat:', error);
    throw error;
  }
};