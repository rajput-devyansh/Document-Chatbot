from document_processor import DocumentProcessor

# Initialize the document processor
processor = DocumentProcessor()

# Process a document
file_path = "data/a_scandal_in_bohemia.pdf"

try:
    # Use the method you just created to load the document and store the result
    documents = processor.load_document(file_path)
    
    # Print the content of the first page of the loaded document
    # Access the page_content attribute of the page at index 0
    if documents:
        print("--- First Page Content ---")
        print(documents[0].page_content)
    else:
        print("The document is empty.")
        
except ValueError as e:
    # Print the error message if a ValueError is raised
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")