import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)


def build_prompt(query, context_chunks):
    
    context_text = ""
    sources = []
    
    for doc, score in context_chunks:
        
        context_text += doc.page_content + "\n\n"
        sources.append(f"{doc.metadata['chunk_id']} with score: {score}")
        


    prompt = f"""
    You are a telecom expert assistant.

    Answer ONLY using the context below.
    If the answer is not explicitly in the context, say "I don't know".

    Context:
    {context_text}

    Question:
    {query}

    Answer:
    """
    return prompt
