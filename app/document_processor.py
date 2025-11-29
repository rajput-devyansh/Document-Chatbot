from langchain_community.document_loaders import PyPDFLoader

class DocumentProcessor:
    
    def load_document(self, file_path):
        """
        Loads a document if it is a PDF.
        Raises ValueError for unsupported formats.
        """
        # Check if the file path ends with '.pdf'
        if file_path.lower().endswith('.pdf'):
            # Create a PyPDFLoader instance with the file path
            loader = PyPDFLoader(file_path)
            # Return the loaded documents
            return loader.load()
        else:
            # If it's not a PDF, raise a ValueError with an appropriate message
            raise ValueError(f"Unsupported file format: {file_path}. Only .pdf files are supported.")