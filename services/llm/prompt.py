def build_prompt(query, context_chunks):
    
    context_text = ""
    # sources = []
    
    for doc in context_chunks:
        
        context_text += doc + "\n\n"
        # sources.append(f"{doc.metadata['chunk_id']} with score: {score}")
        


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
