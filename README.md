# Chatbot Project

This repository contains the code for a chatbot that uses pre-trained models to provide answers to user queries. The chatbot loads Q&A pairs from a JSON file and uses a PDF corpus for additional context.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Overall Approach](#overall-approach)
- [Frameworks/Libraries/Tools Used](#frameworkslibrariestools-used)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Scope](#future-scope)
- [Demo Video](#demo-video)

## Installation

### Prerequisites

- Python 3.7+
- Git

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/nishabhartimishra/Chatbot-Project.git
    cd Chatbot-Project
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Ensure you have the required files:**
    - `Sample Question Answers.json`
    - `Corpus.pdf`

2. **Run the Flask application:**
    ```sh
    python app.py
    ```

3. **Open the chatbot interface:**
    - Open a web browser and navigate to `http://127.0.0.1:5000`.

4. **Interact with the chatbot:**
    - The chatbot will greet you with "Hello! How can I assist you today?"
    - You can then type your queries into the chat interface.

## Project Structure

Chatbot-Project/
│
├── app.py
├── chat.html
├── Corpus.pdf
├── Sample Question Answers.json
├── requirements.txt
├── static/
│ └── wine_video.mp4
└── README.md

## Overall Approach

1. **Loading Q&A Pairs:**
   - Load Q&A pairs from a JSON file.

2. **Extracting Text from PDF:**
   - Extract text from a provided PDF file.

3. **Combining Data:**
   - Combine the Q&A pairs with the extracted text from the PDF.

4. **Encoding Data:**
   - Use a pre-trained model to encode the questions from the Q&A pairs.

5. **Flask API:**
   - Create a Flask API endpoint to handle user queries.
   - Use the SentenceTransformer model to find the best match for user queries.

6. **Frontend Interface:**
   - Create a simple chat interface using HTML, CSS, and JavaScript.
   - Display the chatbot's greeting message upon loading.

## Frameworks/Libraries/Tools Used

- **Flask**: For creating the web API.
- **SentenceTransformer**: For encoding and finding the best match for user queries.
- **PyPDF2**: For extracting text from PDF files.
- **Flask-CORS**: For handling CORS in the Flask application.

## Challenges and Solutions

- **PDF Text Extraction**: 
  - Challenge: Ensuring text is correctly extracted from various PDF formats.
  - Solution: Use `PyPDF2` to reliably extract text.

- **Model Performance**:
  - Challenge: Ensuring the chatbot provides accurate answers.
  - Solution: Tune the similarity threshold for better matching.

## Future Scope

- **Improving Model Accuracy**: 
  - Experiment with different pre-trained models or fine-tune a model for specific domains.

- **Adding More Data Sources**: 
  - Incorporate additional data sources like databases or APIs to enhance the chatbot's knowledge base.

- **Enhancing Frontend Interface**: 
  - Create a more interactive and user-friendly frontend interface.

## Demo Video

A one-minute video showing the chatbot in action is included in the repository.

## Contact

For any queries, please contact mishranishabharti@gmail.com.

