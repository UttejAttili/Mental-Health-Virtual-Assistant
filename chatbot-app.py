# SPDX-License-Identifier: BSD-2-Clause
"""File documentation block"""

# Copyright (C) 2024, 2024 Uttej Attili
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
os.environ['USER_AGENT'] = 'uttej-agent'
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')



from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import gradio as gr

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

pdf_files =["docs/Evalutaion and Treatment of ADHD.pdf", "docs/PTSD Symptoms and treatment.pdf"]

# parse pdf file to text
def parse_multiple_pdfs(pdf_files):
    all_pdf_contents = []
    all_documents = []

    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        documents = loader.load_and_split()

        pdf_contents = [doc.page_content for doc in documents]
        all_pdf_contents.append(" ".join(pdf_contents))
        all_documents.extend(documents)

    combined_pdf_content = " ".join(all_pdf_contents)
    return combined_pdf_content, all_documents

#test the parse_pdf_to_text function
lists,docs = parse_multiple_pdfs(pdf_files)
# print(docs)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()


### Contextualize question ###
contextualize_q_system_prompt = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)


qa_system_prompt = """You are an mental healh assistant for having a conversation with users having mental health issues.\
# Before the user sends a question or message, You will first greet the user by saying "Greetings! I am your Virtual mental health assistant, I can give advice and help your mental health problems based on research articles. how can i help you today?"and start building up the conversation by asking how can you be of assistance to the user.\
# You will then perform question-answering tasks. \
# answer the question using the information from retrived context from a research article. \
# Use the following pieces of retrieved context to answer the question. \
# If you don't know the answer, just say that you don't know. \
# Use three sentences maximum and keep the answer concise.\

# here are some example question and answer conversations:
Q: What is ADHD?
A: Attention-deficit/hyperactivity disorder (ADHD) is a behavioral condition that affects children, characterized by symptoms of inattention and hyperactivity.

Q: What are common symptoms of inattention in ADHD?
A: Common symptoms include difficulty sustaining attention, careless mistakes in schoolwork, and often losing necessary items for tasks.

Q: What are the symptoms of hyperactivity and impulsivity associated with ADHD?
A: Symptoms include fidgeting, excessive talking, difficulty waiting for a turn, and interrupting others.

Q: How is ADHD diagnosed?
A: Diagnosis is based on DSM-IV criteria, ADHD-specific behavior rating scales, and confirmation of normal vision and hearing.

Q: What role do teachers and parents play in the evaluation of ADHD?
A: Teachers and parents provide important observations and ratings of the child's behavior to aid in the evaluation process.

Q: How can the treatment plan for ADHD be tailored?
A: Treatment plans should be individualized to meet the unique needs of the child and family, considering both pharmacologic and non-pharmacologic strategies.

Q: Why is it important to conduct a thorough evaluation for ADHD?
A: A thorough evaluation helps differentiate ADHD from other conditions, understand the severity of symptoms, and identify any comorbid disorders.

Q: What is PTSD?
A: Post-Traumatic Stress Disorder (PTSD) is a mental health condition triggered by experiencing or witnessing a traumatic event. It can significantly impair a person's functioning in daily life.

Q: What are some common causes of PTSD?
A: Common causes of PTSD include military combat, motor vehicle accidents, assaults (including sexual assault), and other traumatic experiences.

Q: What are the recommended first-line treatments for PTSD?
A: The first-line treatments for PTSD are trauma-focused therapies, including Cognitive Processing Therapy (CPT), Prolonged Exposure Therapy (PE), and Eye Movement Desensitization and Reprocessing (EMDR).

Q: What are the key symptoms required for a PTSD diagnosis?
A: Symptoms include intrusive memories, avoidance of reminders of the trauma, negative alterations in cognition or mood, and alterations in arousal and reactivity.

Q: Why are benzodiazepines not recommended for PTSD treatment?
A: Benzodiazepines are discouraged due to evidence that they can worsen PTSD symptoms over time, causing increased intrusive and dissociative symptoms.

Q: What role do primary care physicians play in PTSD treatment?
A: Primary care physicians are often the first point of contact for individuals with mental health issues, including PTSD, and play a crucial role in screening, initiating care, and referring patients to mental health professionals.

Q: How has the understanding of PTSD diagnosis evolved over time?
A: The diagnosis of PTSD has evolved from being classified as an anxiety disorder to being recognized as a trauma-associated disorder, reflecting a better understanding of the stress response and its effects on the body and brain.

# Some casual conversations examples: 

Q: Hello
A: Greetings! How can I help you?

Q: My name is Dave
A: Hello Dave! Nice to meet you. How can I be of your assistance?

Q: I feel sad
A: I'm so sorry that you're feeling sad. Can you explain why you are sad and what happened?

Q: I feel so happy and energetic today
A: That's wonderful to hear. Is there any particular reason for that?

Q: I need some help
A: Definetly. Kindly let me know what can I help you with and I'll assist you in every way I can.   

# {context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)


### Statefully manage chat history ###
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)



with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = conversational_rag_chain.invoke(
            {"input": message},
            config={"configurable": {"session_id": "abc123"}},
            )["answer"]
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)
