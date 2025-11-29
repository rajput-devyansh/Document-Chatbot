# 1. CHANGED: Import Ollama instead of OpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

class ChatEngine:
    def __init__(self):
        # 2. CHANGED: Initialize ChatOllama with your specific hardware settings
        self.chat_model = ChatOllama(
            model="gemma3:4b",  # The 4B model fits your 6GB VRAM perfectly
            temperature=0,      # 0 makes it stick strictly to facts (good for RAG)
        )
        
        self.system_message = (
            "You are a helpful assistant that ONLY answers questions based on the "
            "provided context. If no relevant context is provided, do NOT answer the "
            "question and politely inform the user that you don't have the necessary "
            "information to answer their question accurately."
        )
        
        # Define the prompt template (This logic remains the same)
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(self.system_message),
            HumanMessagePromptTemplate.from_template(
                "Context:\n{context}\n\nQuestion: {question}"
            )
        ])
        
        # Keep conversation history for display/logging
        self.conversation_history = []

    def send_message(self, user_message, context=""):
        """Send a message to the chat engine and get a response"""
        # Format the messages
        messages = self.prompt.format_messages(
            context=context,
            question=user_message
        )
        
        # Get the response from the local Ollama model
        response = self.chat_model.invoke(messages)
        
        # Track history
        self.conversation_history.append(HumanMessage(content=user_message))
        self.conversation_history.append(AIMessage(content=response.content))
        
        return response.content

    def reset_conversation(self):
        """Reset the conversation history"""
        self.conversation_history = []