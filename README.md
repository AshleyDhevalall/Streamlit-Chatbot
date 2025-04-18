# Streamlit-Chatbot

## Introduction
Building a chatbot using Streamlit, LangChain, and Ollama.  This chatbot will run locally and allow us to chat with powerful models like LLaMA 3.2 and DeepSeek.

Prerequisites
Before we begin, ensure you have the following:

Python (>=3.8)
pip installed
Streamlit, LangChain, and Ollama installed
Step 1: Installing Ollama and AI Models
Ollama is a powerful tool for running local AI models efficiently. Follow these steps to install Ollama and load AI models.

1.1 Install Ollama
For MacOS & Linux, run:

curl -fsSL https://ollama.com/install.sh | sh
For Windows, download the installer from Ollama’s website and follow the instructions.

1.2 Install AI Models
Once Ollama is installed, you can pull AI models:

LLaMA 3.2:
ollama pull llama3.2
DeepSeek 1.5B:
ollama pull deepseek-r1:1.5b
These commands will download and prepare the models for use.

Step 2: Install Required Python Libraries
We need Streamlit, LangChain, and other dependencies. Install them using:
pip install -r requirements.txt

Step 3: Running the Chatbot
Save the code as chatbot.py, then run:

streamlit run chatbot.py
This will launch a local web app where you can chat with AI models.

you can access the app using http://localhos:8051
