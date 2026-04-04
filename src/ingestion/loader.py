from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents(data_path="data/"):
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()
    
    print(f"Loaded {len(documents)} pages")
    
    return documents

