import gradio as gr
import re

# Enhanced rule-based logic with regex + basic Hindi/English support
chat_history = []

def rule_bot(user_input):
    global chat_history
    user_input = user_input.lower()

    # Regex patterns
    patterns = {
        r"\b(hi|hello|hey|namaste)\b": "Hello! 😊 How can I help you today? / नमस्ते! क्या मैं आपकी मदद कर सकता हूँ?",
        r"\b(your name|tumhara naam|naam kya)\b": "I am a rule-based bot. / मैं एक rule-based chatbot हूँ.",
        r"\b(weather|mausam)\b": "I cannot give live weather, but it’s always sunny here! / मैं लाइव मौसम नहीं बता सकता, लेकिन यहां की गगा ऐसी है!",
        r"\b(bye|goodbye|alvida)\b": "Goodbye! 👋 Have a nice day! / अलविदा! अच्छा दिन रहे!"
    }

    # Matching rules
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            chat_history.append((user_input, response))
            return format_chat(chat_history)

    fallback = "Sorry, I didn't understand that. / क्षमा क्या आप कहना चाहते हैं, मुझे समझ नहीं आया."
    chat_history.append((user_input, fallback))
    return format_chat(chat_history)


def format_chat(history):
    # Format chat history for display
    formatted = ""
    for user, bot in history[-5:]:  # Show last 5 interactions
        formatted += f"You: {user}\nBot: {bot}\n\n"
    return formatted


def reset_chat():
    global chat_history
    chat_history = []
    return "Chat history cleared. Start a new conversation!"

# Gradio UI
iface = gr.Interface(
    fn=rule_bot,
    inputs=gr.Textbox(lines=2, placeholder="Type a message in English or Hindi..."),
    outputs="text",
    title="🤖 Rule-Based Chatbot (English/Hindi)",
    description="Chat with simple rule-based logic using regex."
)

# Add Clear button
iface = iface.queue().launch(share=True)
