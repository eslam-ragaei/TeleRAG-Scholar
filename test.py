import gradio as gr

def greet(name):
    return f"Hello {name}!"

with gr.Blocks() as demo:
    # 1. Define Components
    name_input = gr.Textbox(label="Enter your name")
    output_text = gr.Textbox(label="Greeting")
    submit_btn = gr.Button("Submit")

    # 2. Define the Click Event
    submit_btn.click(
        fn=greet,           # The function to run
        inputs=name_input,  # Component(s) providing data to the function
        outputs=output_text # Component(s) to be updated by the function
    )

demo.launch()
