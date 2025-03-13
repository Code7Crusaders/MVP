class ChatController:
    """
    Controller class to manage chat interactions.
    """
    def __init__(self):
        pass  # Initialize if needed, for example, with services or use cases

    def get_messages(self, quantity: int):
        """
        Dummy function to simulate message retrieval based on the quantity.
        Args:
            quantity (int): The number of messages to retrieve.
        Returns:
            list: A list of dummy messages.
        """
        # Generate dummy messages
        return [{"id": i, "text": f"Message {i}"} for i in range(quantity)]
