import gradio as gr
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline

# Step 1: Load PDF
loader = PyPDFLoader("Business_Economics.pdf")
documents = loader.load()

# Step 2: Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Step 3: Create embeddings and FAISS vector DB
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.from_documents(docs, embedding_model)
retriever = vector_db.as_retriever()

# Step 4: Load LLM
llm_pipeline = pipeline("text-generation", model="gpt2", max_new_tokens=200)
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Step 5: RAG Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 6: Gradio UI
def chatbot(query):
    return qa_chain.run(query)

ui = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, label="Aapka Sawal"),
    outputs=gr.Textbox(label="Chatbot ka Jawaab"),
    title="📄 Rahul PDF Chatbot",
    description="Ye chatbot rahul.pdf file se knowledge le kar jawaab deta hai."
)

ui.launch()