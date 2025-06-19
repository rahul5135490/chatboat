import gradio as gr

# Rule-based logic
def rule_based_bot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot."
    elif "weather" in user_input:
        return "I cannot tell you live weather, but it's always sunny in code-land!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that yet."

# Gradio UI
iface = gr.Interface(
    fn=rule_based_bot,
    inputs=gr.Textbox(lines=2, placeholder="Type your message..."),
    outputs="text",
    title="🤖 Rule-Based Chatbot",
    description="A simple chatbot that replies using if-else rules."
)

iface.launch()
