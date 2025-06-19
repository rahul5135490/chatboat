# retrieval_chatbot.py
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# QnA Knowledge Base
qa_pairs = {
    "What is your name?": "I am a simple chatbot.",
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Python?": "Python is a popular programming language.",
    "What is Gradio?": "Gradio is a Python library to create ML web apps easily.",
    "Who developed ChatGPT?": "ChatGPT was developed by OpenAI."
}

# Load Sentence Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert questions to vectors
questions = list(qa_pairs.keys())
question_vectors = model.encode(questions)

# Create FAISS index
dimension = question_vectors[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(question_vectors))

# Prediction function
def chatbot(user_input):
    query_vector = model.encode([user_input])
    D, I = index.search(np.array(query_vector), k=1)
    matched_question = questions[I[0][0]]
    return qa_pairs[matched_question]

# Gradio UI
demo = gr.Interface(fn=chatbot,
                    inputs=gr.Textbox(lines=2, placeholder="Ask a question..."),
                    outputs="text",
                    title="🔎 Retrieval-based Chatbot",
                    description="Ask questions related to a small knowledge base. Based on semantic similarity.")

demo.launch()
