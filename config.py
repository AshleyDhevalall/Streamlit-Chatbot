"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""

class Config:
    PAGE_TITLE = "Streamlit Ollama Chatbot"

    OLLAMA_MODELS = ('phi3:latest', 'phi4-mini:latest', 'mistral:latest', 'nomic-embed-text:latest',  
                        'llama3.2:latest', 'deepseek-r1:latest', 'sentiments:latest', 'mistral-openorca:latest',    
                        'llama3:latest', 'gemma:2b')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""                 
    