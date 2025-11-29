from rag_chatbot import RAGChatbot
import os

# Initialize the document processor
chatbot = RAGChatbot()

# Get the directory where THIS script is located to safely find data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_dir, "data")
query = "what is the plot of the story?"

if os.path.exists(data_directory):
    for filename in os.listdir(data_directory):
        file_path = os.path.join(data_directory, filename)
        chatbot.upload_document(file_path)
        print(f"Query: {query}")
        response = chatbot.send_message(query)
        print("AI Response:")
        print(response)
        print("-" * 30) # Separator
        chatbot.reset_all()
else:
    print(f"Error: Directory '{data_directory}' not found.")