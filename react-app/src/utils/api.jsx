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

// Save a new conversation title
export const saveConversationTitle = async (title) => {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Authentication token is missing');
  }

  try {
    const response = await fetch('http://127.0.0.1:5001/conversation/save_title', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ title }), // Send the title as a flat object
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to save conversation title');
    }

    const data = await response.json();
    console.log('Conversation title saved:', data);
    return data;
  } catch (error) {
    console.error('Error saving conversation title:', error);
    throw error;
  }
};

// Delete a specific conversation
export const deleteConversation = async (conversationId) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch(`http://127.0.0.1:5001/conversation/delete/${conversationId}`, {
      method: 'DELETE',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to delete conversation');
    }

    const data = await response.json();
    console.log('Conversation deleted:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error deleting conversation:', error);
    throw error;
  }
};

export const updateMessageRating = async (messageId, rating) => {
  const token = localStorage.getItem('token');
  try {
    const response = await fetch('http://127.0.0.1:5001/message/update_rating', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        id: messageId,
        rating: rating,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to update message rating');
    }

    const data = await response.json();
    console.log('Message rating updated:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error updating message rating:', error);
    throw error;
  }
};

export const saveSupportMessage = async (supportMessageData) => {
  const token = localStorage.getItem('token'); // Retrieve the JWT token from localStorage

  if (!token) {
    console.error('Error: No token found in localStorage'); // Debugging log
    throw new Error('Authentication token is missing');
  }

  console.log('Support message data to save:', supportMessageData); // Debugging log

  try {
    const response = await fetch('http://127.0.0.1:5001/support_message/save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`, // Add the Authorization header with the token
      },
      body: JSON.stringify(supportMessageData), // Send the support message data as JSON
    });

    console.log('Response status:', response.status); // Debugging log

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Error response from server:', errorData); // Debugging log
      throw new Error(errorData.error || 'Failed to save support message');
    }

    const data = await response.json();
    console.log('Support message saved:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error saving support message:', error); // Debugging log
    throw error;
  }
};

export const fetchSupportMessages = async () => {
  const token = localStorage.getItem('token'); // Recupera il token di autenticazione

  if (!token) {
    throw new Error('Authentication token is missing');
  }

  try {
    const response = await fetch('http://127.0.0.1:5001/support_message/get_all', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`, // Aggiunge il token nell'header
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to fetch support messages');
    }

    const data = await response.json();
    console.log('Fetched support messages:', data); // Log per debugging
    return data;
  } catch (error) {
    console.error('Error fetching support messages:', error); // Log per debugging
    throw error;
  }
};

export const markSupportMessageDone = async (supportMessageId) => {
  const token = localStorage.getItem('token'); // Retrieve the JWT token from localStorage

  if (!token) {
    throw new Error('Authentication token is missing');
  }

  try {
    const response = await fetch(`http://127.0.0.1:5001/support_message/mark_done/${supportMessageId}`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`, // Add the Authorization header with the token
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to mark support message as done');
    }

    const data = await response.json();
    console.log('Support message marked as done:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error marking support message as done:', error); // Debugging log
    throw error;
  }
};

export const fetchDashboardMetrics = async () => {
  const token = localStorage.getItem('token'); // Retrieve the JWT token from localStorage

  if (!token) {
    throw new Error('Authentication token is missing');
  }

  try {
    const response = await fetch('http://127.0.0.1:5001/dashboard/metrics', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`, // Add the Authorization header with the token
      },
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to fetch dashboard metrics');
    }

    const data = await response.json();
    console.log('Fetched dashboard metrics:', data); // Debugging log
    return data;
  } catch (error) {
    console.error('Error fetching dashboard metrics:', error); // Debugging log
    throw error;
  }
};

