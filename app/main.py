from document_processor import DocumentProcessor
import os

# Initialize the document processor
processor = DocumentProcessor()

# Get the directory where THIS script is located to safely find data
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "a_scandal_in_bohemia.pdf")

try:
    print(f"Processing document: {file_path}")
    
    # Process the document (Load -> Split -> Vectorize)
    processor.process_document(file_path)
    print("Document processed successfully.")

    # Define a query
    query = "What is the main mystery in the story?"

    # Use the method to retrieve relevant context
    print(f"\nQuerying: {query}")
    relevant_docs = processor.retrieve_relevant_context(query)

    # Check if any relevant documents were found
    if relevant_docs:
        print("\n--- Relevant Context Found ---")
        # Print the content of the first one
        print(relevant_docs[0].page_content)
    else:
        print("No relevant documents found.")
        
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")