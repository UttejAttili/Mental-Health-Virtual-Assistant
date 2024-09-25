# Mental-Health-Virtual-Assistant
This repository is a simple implementation of a chatbot that acts as a mental health virtual assistant. 

Overview:
This project is a virtual mental health assistant chatbot designed to help users by providing information and advice based on research articles related to mental health, specifically ADHD and PTSD. The chatbot interacts with users, understands their emotional state, and offers brief and concise responses to their queries. It uses natural language processing (NLP) models to retrieve context and deliver answers sourced from research articles.


The chatbot is built using the following tools:

-> LangChain for managing the interaction with OpenAI models and handling the chat flow.
-> OpenAI GPT-4 model for generating human-like responses and retrieving information from documents.
-> Chroma for document retrieval and embeddings storage.
-> Gradio for building an easy-to-use web interface for chatbot interaction.
-> PDF document parsing to extract relevant mental health information about ADHD and PTSD from research articles.

Features:
Conversational Interface: The chatbot engages users in a conversation, making it easier to discuss mental health issues in a supportive environment.
ADHD & PTSD Knowledge Base: The chatbot draws from PDF research documents on ADHD and PTSD to answer questions and provide relevant advice.
History-Aware Responses: The chatbot keeps track of previous chat history to maintain context during conversations.
Simple, Brief Answers: Each response is capped at three sentences, ensuring that the information is concise and easy to digest.
Gradio Interface: A user-friendly interface that allows users to interact with the chatbot in a web-based environment.


Installation:

To set up and run this project locally, follow these steps:

1) Clone the repository:
git clone https://github.com/UttejAttili/Mental-Health-Virtual-Assistant.git
cd Mental-Health-Virtual-Assistant

2) Install the required dependencies:
pip install -r requirements.txt

3) Set up your OpenAI API key and user agent by replacing the placeholders in the os.environ section with your credentials:
os.environ['USER_AGENT'] = 'your-agent'
os.environ['OPENAI_API_KEY'] = 'your-api-key'

4) Ensure the PDF files for ADHD and PTSD research articles are placed in the docs/ directory:
Evaluation and Treatment of ADHD.pdf
PTSD Symptoms and Treatment.pdf

5) Run the application:
python app.py

6) Access the chatbot interface:
The Gradio app will generate a shareable link in the terminal. Use the link to access the chatbot in your browser.


Project Structure:

mental-Health-Virtual-Assistant/
│
├── chatbot-app.py                        # Main application script to launch the chatbot
├── docs/                         # Folder containing PDF research articles
│   ├── Evaluation and Treatment of ADHD.pdf
│   ├── PTSD Symptoms and Treatment.pdf
├── requirements.txt              # Python dependencies
└── README.md      

Future Improvements:

1) Expand Knowledge Base: Adding more research articles and documentation to cover a wider range of mental health conditions.
2) User Mood Detection: Implementing a more advanced mood detection system for better response generation.
3) Improved Conversation Flow: Enhancing the conversation flow for better user interaction and emotional support.
