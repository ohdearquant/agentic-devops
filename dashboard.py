import gradio as gr
import time

# Simulated LLM function
def llm_workflow(input_text):
    start_time = time.time()
    # Simulate processing
    time.sleep(2)
    output_text = f"Processed: {input_text}"
    end_time = time.time()
    response_time = end_time - start_time
    token_usage = len(input_text.split())
    return output_text, response_time, token_usage

def main():
    with gr.Blocks() as demo:
        gr.Markdown("# LLM Workflow Composition Observe Dashboard")

        with gr.Row():
            with gr.Column():
                input_text = gr.Textbox(label="Input Text")
                submit_button = gr.Button("Submit")
            with gr.Column():
                output_text = gr.Textbox(label="Output Text", interactive=False)
                response_time = gr.Number(label="Response Time (s)", interactive=False)
                token_usage = gr.Number(label="Token Usage", interactive=False)

        logs = gr.Textbox(label="Logs", interactive=False, lines=10)

        def run_workflow(input_text):
            output, time_taken, tokens = llm_workflow(input_text)
            logs.update(f"Input: {input_text}\nOutput: {output}\nTime Taken: {time_taken}s\nTokens Used: {tokens}")
            return output, time_taken, tokens

        submit_button.click(run_workflow, inputs=input_text, outputs=[output_text, response_time, token_usage])

    demo.launch()

if __name__ == "__main__":
    main()
