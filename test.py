from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Create a ChatOpenAI instance
chat = ChatOllama(
    model="gemma3:4b",
    max_tokens=150
)

conversations = {}
# Create a counter for generating chat IDs starting from 0
chat_id_counter = 0

# Create a function called create_new_chat
def create_new_chat():
    global chat_id_counter
    # Creates a new conversation with the default system prompt
    new_chat_history = [
        SystemMessage(content="You are a tour guide")
    ]
    # Adds this new conversation to your dictionary using a unique ID
    current_id = chat_id_counter
    conversations[current_id] = new_chat_history
    
    # Increases your ID counter for the next conversation
    chat_id_counter += 1
    
    # Returns the ID so you can reference this specific conversation later
    return current_id

# Modify the send_message function to take a chat_id
def send_message(chat_id, user_input):
    # Retrieve the correct conversation using the chat_id
    if chat_id not in conversations:
        return "Error: Chat ID not found."
    
    messages = conversations[chat_id]
    
    # Add the user's message to the specific conversation
    messages.append(HumanMessage(content=user_input))
    
    # Get the AI's response using the specific history
    response = chat.invoke(messages)
    
    # Add the AI's response to the specific conversation history
    messages.append(AIMessage(content=response.content))
    
    # Return the content of the AI's response
    return response.content

# Create two separate chat instances and store their IDs
chat_id_1 = create_new_chat()
chat_id_2 = create_new_chat()

print(f"Created Chat 1 (ID: {chat_id_1}) and Chat 2 (ID: {chat_id_2})\n")

# Send a question about Paris to the first chat
response_1 = send_message(chat_id_1, "What is a must-visit landmark in Paris?")
print(f"Chat {chat_id_1} (Paris): {response_1}\n")

# Send a question about Rome to the second chat
response_2 = send_message(chat_id_2, "What is a famous historic site in Rome?")
print(f"Chat {chat_id_2} (Rome): {response_2}\n")

# Send a vague follow-up question about restaurants to each chat
# This demonstrates that Chat 1 knows we mean Paris, and Chat 2 knows we mean Rome
print("-" * 30)
follow_up_1 = send_message(chat_id_1, "Are there any good restaurants nearby?")
print(f"Chat {chat_id_1} Follow-up: {follow_up_1}\n")

follow_up_2 = send_message(chat_id_2, "Are there any good restaurants nearby?")
print(f"Chat {chat_id_2} Follow-up: {follow_up_2}")