from flask import Flask, request, jsonify, send_from_directory
from sentence_transformers import SentenceTransformer, util
import torch
import json
from PyPDF2 import PdfReader
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load the Q&A pairs from the JSON file
with open('Sample Question Answers.json', 'r') as file:
    sample_qa_data = json.load(file)

# Extract text from the PDF corpus
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

corpus_text = extract_text_from_pdf('Corpus.pdf')

# Combine the Q&A pairs with the extracted corpus text
corpus = []
for item in sample_qa_data:
    corpus.append({"question": item['question'], "answer": item['answer']})

# Load pre-trained model and encode corpus questions
model = SentenceTransformer('all-MiniLM-L6-v2')
corpus_embeddings = model.encode([qa['question'] for qa in corpus], convert_to_tensor=True)

@app.route('/')
def index():
    return send_from_directory('.', 'chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if user_message.lower() == "start":
        return jsonify({"answer": "Hello! How can I assist you today?"})

    user_embedding = model.encode(user_message, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(user_embedding, corpus_embeddings)[0]
    best_match_idx = torch.argmax(cos_scores).item()

    if cos_scores[best_match_idx] >= 0.7:  # Threshold for considering a match
        answer = corpus[best_match_idx]['answer']
    else:
        answer = "Please contact the business directly for further assistance."

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
