# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
from pyarrow import proxy_memory_pool

load_dotenv(dotenv_path='.env')

# os.environ[ "OPENAI_API_KEY"]=os.getenv("'OPENAI_API_KEY")
## Langsmith Tracking
os.environ ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful assistant. Please response to user queries"),
        ('user', "Question : {question}")
    ]
)

## Streamlit framework
st.title("Langchain Demo With Gemma3:4b")
imput_text = st.text_input("Search the topic you want")

## Ollama LLM
llm = Ollama(model="Gemma3:4b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if imput_text:
    st.write(chain.invoke({'question': imput_text}))
