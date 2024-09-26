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

Workflow Architecture:
![Application](https://github.com/UttejAttili/mental-Health-Virtual-Assistant/blob/main/screenshots/Application.jpeg)



Installation:

To set up and run this project locally, follow these steps:

1) Clone the repository:
git clone https://github.com/UttejAttili/Mental-Health-Virtual-Assistant.git

cd Mental-Health-Virtual-Assistant

3) Install the required dependencies:
pip install -r requirements.txt

4) Set up your OpenAI API key and user agent by replacing the placeholders in the os.environ section with your credentials:
os.environ['USER_AGENT'] = 'your-agent'
os.environ['OPENAI_API_KEY'] = 'your-api-key'

5) Ensure the PDF files for ADHD and PTSD research articles are placed in the docs/ directory:
Evaluation and Treatment of ADHD.pdf
PTSD Symptoms and Treatment.pdf

6) Run the application:
python app.py

7) Access the chatbot interface:
The Gradio app will generate a shareable link in the terminal. Use the link to access the chatbot in your browser.


Project Structure:
```bash
mental-Health-Virtual-Assistant/
│
├── chatbot-app.py                        # Main application script to launch the chatbot
├── docs/                         # Folder containing PDF research articles
│   ├── Evaluation and Treatment of ADHD.pdf
│   ├── PTSD Symptoms and Treatment.pdf
├── requirements.txt              # Python dependencies
└── README.md      
```

Deploying the application on AWS: 

requirements:
-> AWS EC2
-> Github

Here's how I deployed my implementation on AWS using EC2 instance and ran the application. 

1) create a folder in local machine (Visual Studio Code) and implement the whole project with appropriate files required. organize the folder structure as required. 

2) create a new repository in github for the project and push the whole project folder from local machine to the new repository. 

Steps to create a new repository and push the folder to github:

-> Create a new repository in github
-> Initialize Git in your project directory:
	command: git init
-> Add your project files to the staging area:
	command: git add .
->  Commit your changes:
	command: git commit -m "Initial commit"
-> Connect your local repository to the remote repository:
	command: git remote add origin <remote_repository_url>
-> Push your local changes to the remote repository:
	command: git push -u origin master

3) create a new EC2 Instance in AWS EC2 console. 

steps to create an AWS EC2 Instance: 

-> Navigate to AWS EC2 Console. click on Instances section. click on Launch Instance
-> Give a name for your server instance. 
-> For Amazon Machine Image, select Ubuntu
-> for Key pair, click on create new key pair. give a name for the key pair. a new key pair will be generated and downloaded in given_name.pem format
-> for network settings, leave it with default options: Create Security group -> Allow SSH traffic form
-> Click on launch instance. The instance will be created and it starts running. 
-> click on the instance, scroll down and navigate to security tab. click on the secutity groups hyperlink. 
-> scroll down to inbound rules section. click on edit inbound rules
-> click on add new rule. set the following:
	type: Custom TCP
	Port range: 7860-7870
	Source: Anywhere Ipv4
-> click on save. The instance will be ready to use

4) To connect to the instance, you must complete two steps:
	1- You must be the owner of the key-pair file. We will demonstrate how to
	achieve this on both Windows and Linux/macOS platforms.
	For Windows users:
	1. Right-click the key-pair file
	2. Go to properties
	3. Navigate to the security tab
	4. Click “Advanced”
	5. Inspect permission entries. If your username is absent, click “change”
	(admin privileges required) to add your username, and subsequently,
	remove all other privileges from SYSTEM and Administrators.
	
5) In the terminal, Navigate to the folder where the key pair file is present and execute the following command:
	
->	ssh -i path_to_your_keypair_file.pem ec2-user@Public-IPv4-address
	
Note: the use of “ec2-user” before the “@” symbol may not always be applicable; it depends on your instance. To determine the correct username, click on the instance, navigate to “Connect, ” and under the “EC2 instance connect” tab, you will find the required username. Moreover, you can locate your Public IPv4 address in your EC2 instance panel.

6) Once you connect to your EC2 instance, configure it by doing the following process:
	
->	Initiate a system update:
	command: sudo apt-get update
->	Install Git:
	command: sudo apt-get install git
->	Install Pip:
	command: sudo apt-get install python3-pip
->	Clone your GitHub repository:
	command: git clone your_repository_url
-> Navigate into the folder of the project in the instance: 
	command: cd <folder_name>
->  create a virtual environment in the instance and activate it: 
	commands: 
	 -> python3 -m venv venv
	 -> source venv/bin/activate
-> install the required packages to run the project in Virtual Machine
	command: pip install -r requirements.txt
-> run your script to run the application: 
	command: python script_name.py

The application will start running and the url will be provided in the terminal. Copy the URL and paste it in the web browser and test the application. 


Future Improvements:

1) Expand Knowledge Base: Adding more research articles and documentation to cover a wider range of mental health conditions.
2) User Mood Detection: Implementing a more advanced mood detection system for better response generation.
3) Improved Conversation Flow: Enhancing the conversation flow for better user interaction and emotional support.

Reference: https://abdulrahman-almutlaq.medium.com/deploying-gradio-on-aws-a-beginners-quick-start-guide-85a01f269945
		       https://python.langchain.com/docs/tutorials/rag/
