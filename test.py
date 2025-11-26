from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

# Create a ChatOpenAI instance
chat = ChatOllama(
    model="gemma3:4b",
    max_tokens=150
)

#Ask the AI a different question
response = chat.invoke([
    SystemMessage(content="You are a strict math assistant. If a question is not about mathematics, you must refuse to answer it completely and strictly. Do not provide any information for non-math queries."),
    HumanMessage(content="Can you tell a poem about the beauty of nature?")
])

# Print the AI's response
print("AI Response:")
print(response.content)