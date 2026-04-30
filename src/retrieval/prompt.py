import sys
import os
# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from langchain_ollama import OllamaLLM
# from query_data import search_db , build_context

PROMPT_TEMPLATE = """
Answer ONLY using the context below.
If the answer is not explicitly in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

# generate the llm input to generate the answer

def generate_answer(context, query):
    
    model = OllamaLLM(
    model="mistral",
    temperature=0.0,
    
)
    
    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=query
    )

    response = model.invoke(prompt)
    
    return response


if __name__ == "__main__":
    
    print("Use app.py with gradio UI interface")
    
    # query = input("Enter the question you want:\n--> ")
    
    # search_results = search_db(query=query)
    
    # context , source = build_context(search_results)
    
    # answer = generate_answer(context=context , query=query)
    
    # print(answer)
    # with open("_output.txt", "w") as file:
    #     file.write(answer)
    # print("*"*100)
    # for s in source:
    #     print(s)