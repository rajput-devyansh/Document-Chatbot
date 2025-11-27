from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model="nomic-embed-text:v1.5")

# Create a HumanMessage object
message = SystemMessage(content="LangChain is amazing!")

# Access and print the message type attribute
print("Message type:", message.type)

# Access and print the message content attribute
print("Message content:", message.content)

chat = ChatOllama(
    model="gemma3:4b",
    temperature=0.7,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.3
)