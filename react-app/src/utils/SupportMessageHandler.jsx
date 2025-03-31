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