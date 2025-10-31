from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv


app = FastAPI(
    title="LangChain API",
    version="1.0.0",
    description="LangChain API",
)

add_routes(
    app,
    ChatOllama(),
    path="/ollama"
)

model = Ollama(model="Gemma3:4b")
load_dotenv(dotenv_path=".env")
