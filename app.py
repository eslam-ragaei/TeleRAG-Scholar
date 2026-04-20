import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

import gradio as gr
from src.retrieval.query_data import search_db , build_context
from src.retrieval.prompt import generate_answer
from src.ingestion.populate_database import clear_database , populate_database

def chat(query):
    if not query.strip():
        return "⚠️ Please enter a valid query.", ""

    try:
        search_results = search_db(query=query)
        context, source = build_context(search_results)
        answer = generate_answer(context=context, query=query)
        with open("output.txt", "w") as file:
            for i, (doc, score) in enumerate(search_results):
                file.write(f"\n--- Rank {i+1} ---\n")
                file.write(f"Score: {score:.2f}\n")
                file.write(f"Source: {doc.metadata['chunk_id']} with score: {score}\n")
                file.write("Content Preview:\n")
                file.write(doc.page_content + "\n")
                file.write("*"*100)
                file.write("\n\n\n")
        sources = "\n\n".join(source) if source else "No sources found."
        return answer, sources

    except Exception as e:
        return f"❌ Error: {str(e)}", ""

def clear_db():
    try:
        clear_database()
        return "✅ Database cleared successfully"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def populate_db():
    try:
        populate_database()
        return "✅ Database populated successfully"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Custom CSS for modern, immersive design with equal height containers
custom_css = """
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --dark-bg: #0f0f1e;
    --card-bg: #1a1a2e;
    --text-primary: #ffffff;
    --text-secondary: #a0a0c0;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: var(--dark-bg);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden;
}

.gradio-container {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 1rem 2rem !important;
    background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 100%) !important;
    min-height: 100vh !important;
}

@media (max-width: 768px) {
    .gradio-container {
        padding: 0.5rem 1rem !important;
    }
}

@media (max-width: 480px) {
    .gradio-container {
        padding: 0.5rem !important;
    }
}

.main-header {
    text-align: center;
    padding: 2rem 1rem;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    border-radius: 20px;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    width: 100%;
}

.main-header h1 {
    font-size: 2.5rem;
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.main-header p {
    color: var(--text-secondary);
    font-size: 1.1rem;
}

/* Equal height containers for input and output */
.main-row {
    display: flex !important;
    gap: 1.5rem !important;
    margin-bottom: 1.5rem !important;
    width: 100% !important;
    align-items: stretch !important;
}

.left-column, .right-column {
    flex: 1 !important;
    min-width: 0 !important;
    display: flex !important;
    flex-direction: column !important;
}

.input-container, .output-container {
    background: var(--card-bg) !important;
    border-radius: 15px !important;
    padding: 1.5rem !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    transition: all 0.3s ease !important;
    height: 100% !important;
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
}

.input-container:hover, .output-container:hover {
    border-color: rgba(102, 126, 234, 0.5) !important;
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2) !important;
}

/* Make textareas fill available space */
.query-input, .answer-output {
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

.query-input textarea, .answer-output textarea {
    flex: 1 !important;
    min-height: 400px !important;
    resize: vertical !important;
}

/* Specific heights for different screen sizes */
@media (min-width: 1200px) {
    .query-input textarea, .answer-output textarea {
        min-height: 450px !important;
    }
}

@media (max-width: 1199px) and (min-width: 768px) {
    .query-input textarea, .answer-output textarea {
        min-height: 400px !important;
    }
}

@media (max-width: 767px) {
    .query-input textarea, .answer-output textarea {
        min-height: 300px !important;
    }
}

.source-container {
    background: var(--card-bg) !important;
    border-radius: 15px !important;
    padding: 1.5rem !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    transition: all 0.3s ease !important;
    margin-top: 1rem !important;
    width: 100% !important;
}

.source-container:hover {
    border-color: rgba(102, 126, 234, 0.5) !important;
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2) !important;
}

.source-output textarea {
    min-height: 200px !important;
}

label {
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    margin-bottom: 0.5rem !important;
}

input, textarea {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: var(--text-primary) !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
    width: 100% !important;
}

input:focus, textarea:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.25) !important;
}

button {
    background: var(--primary-gradient) !important;
    border: none !important;
    color: white !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    margin: 0.5rem 0 !important;
    width: 100% !important;
}

button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4) !important;
}

.clear-btn {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
}

.populate-btn {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
}

.status-container {
    background: rgba(255, 255, 255, 0.05) !important;
    border-radius: 10px !important;
    padding: 0.75rem !important;
    margin-top: 1rem !important;
    width: 100% !important;
}

/* Responsive layout */
@media (max-width: 1023px) {
    .main-row {
        flex-direction: column !important;
        gap: 1rem !important;
    }
    
    .left-column, .right-column {
        width: 100% !important;
    }
    
    .main-header h1 {
        font-size: 1.8rem !important;
    }
    
    button {
        padding: 0.6rem 1.2rem !important;
    }
}

@media (max-width: 768px) {
    .gradio-container {
        padding: 0.5rem 1rem !important;
    }
    
    .input-container, .output-container, .source-container {
        padding: 1rem !important;
    }
    
    .main-header {
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    .main-header h1 {
        font-size: 1.5rem !important;
    }
    
    .main-header p {
        font-size: 0.9rem !important;
    }
    
    .query-input textarea, .answer-output textarea {
        min-height: 250px !important;
    }
}

@media (max-width: 480px) {
    .gradio-container {
        padding: 0.5rem !important;
    }
    
    .input-container, .output-container, .source-container {
        padding: 0.75rem !important;
    }
    
    .main-header h1 {
        font-size: 1.2rem !important;
    }
    
    .main-header p {
        font-size: 0.8rem !important;
    }
    
    .section-header h3 {
        font-size: 1rem !important;
    }
    
    label {
        font-size: 0.9rem !important;
    }
    
    .query-input textarea, .answer-output textarea {
        min-height: 200px !important;
    }
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: rgba(102, 126, 234, 0.5);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(102, 126, 234, 0.8);
}

/* Animation for status updates */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.status-container {
    animation: fadeIn 0.5s ease;
}

/* Section headers */
.section-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(102, 126, 234, 0.3);
}

.section-header h3 {
    margin: 0;
    color: var(--text-primary);
    font-size: 1.2rem;
}

/* Database management section */
.button-row {
    display: flex !important;
    gap: 0.75rem !important;
    margin: 1rem 0 !important;
    width: 100% !important;
}

@media (max-width: 480px) {
    .button-row {
        flex-direction: column !important;
    }
}

/* Make all rows full width */
.gradio-row {
    width: 100% !important;
    margin: 0 !important;
}

.gradio-column {
    width: 100% !important;
}

/* Ensure containers take full width */
.container, .block, .tabs, .tab-nav {
    width: 100% !important;
    max-width: 100% !important;
}

/* Fix for button container */
.gradio-row .gr-form-row {
    width: 100% !important;
}

/* Equal height fix for all screen sizes */
.flex-wrap {
    align-items: stretch !important;
}
"""

with gr.Blocks(css=custom_css, title="RAG Chat System", theme=gr.themes.Soft()) as RAG_Chat:
    # Header section
    gr.HTML("""
        <div class="main-header">
            <p>RAG Intelligent Chat System</p>
        </div>
    """)
    
    # Main row with query input (left) and RAG response (right) - equal height
    with gr.Row(elem_classes="main-row"):
        # Left column - Query Input
        with gr.Column(elem_classes="left-column", scale=1):
            with gr.Group(elem_classes="input-container"):
                gr.HTML("""
                    <div class="section-header">
                        <h3>💬 Query Input</h3>
                    </div>
                """)
                query = gr.Textbox(
                    label="Enter your query", 
                    placeholder="Type your question here... The AI will search the database and generate a response based on retrieved context.",
                    lines=5,
                    elem_classes="query-input"
                )
                

        
        # Right column - RAG Response
        with gr.Column(elem_classes="right-column", scale=1):
            with gr.Group(elem_classes="output-container"):
                gr.HTML("""
                    <div class="section-header">
                        <h3>✨ RAG Response</h3>
                    </div>
                """)
                answer = gr.Textbox(
                    label="Generated Answer",
                    placeholder="Your answer will appear here...",
                    lines=12,
                    interactive=False,
                    elem_classes="answer-output"
                )
    with gr.Row():
        with gr.Column():
            submit_btn = gr.Button("🔍 Ask", variant="primary", size="lg")
    # Bottom center - Source Chunks
    with gr.Row():
        with gr.Column(scale=1, min_width=0):
            with gr.Group(elem_classes="source-container"):
                gr.HTML("""
                    <div class="section-header">
                        <h3>📚 Source Chunks</h3>
                    </div>
                """)
                source = gr.Textbox(
                    label="Retrieved Context",
                    placeholder="Source chunks will be displayed here...",
                    lines=8,
                    interactive=False,
                    elem_classes="source-output"
                )
    # Database Management Section
    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group(elem_classes="source-container"):
                gr.HTML("""
                    <div class="section-header">
                        <h3>🛠️ Database Management</h3>
                    </div>
                """)
                
                with gr.Row(elem_classes="button-row"):
                    clear_db_btn = gr.Button("🗑️ Clear DB", elem_classes="clear-btn", size="sm")
                    populate_db_btn = gr.Button("📥 Populate DB", elem_classes="populate-btn", size="sm")
                
                db_status = gr.Textbox(
                    label="📊 Database Status", 
                    placeholder="Ready",
                    interactive=False,
                    elem_classes="status-container"
                )
    
    # Footer
    gr.HTML("""
        <div style="text-align: center; padding: 1rem; margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); color: #a0a0c0; width: 100%;">
            <p>Powered by Advanced RAG | Real-time Context Retrieval</p>
        </div>
    """)

    # Define click events (functions unchanged)
    submit_btn.click(
        fn=chat,
        inputs=query,
        outputs=[answer, source],
        show_progress=True
    )
    
    clear_db_btn.click(
        fn=clear_db,
        outputs=db_status
    )
    
    populate_db_btn.click(
        fn=populate_db,
        outputs=db_status
    )

if __name__ == "__main__":
    RAG_Chat.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )