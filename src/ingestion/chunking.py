from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_documents (documents , chunk_size = 1200 , chunk_overlap = 200):
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    
    all_chunks = []
    for doc in documents:
        chunks = text_splitter.split_documents([doc])
        for i, chunk in enumerate(chunks):
            chunk.metadata['chunk_id'] = f"Source: {doc.metadata['source']} :: Page: {doc.metadata["page"]} :: index: {i}"
            
        all_chunks.extend(chunks)
    print(f"Total chunks created: {len(all_chunks)}")
        
    return all_chunks

