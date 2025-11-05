from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.chat_models import ChatOllama
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI(
    title="LangChain API",
    version="1.0.0",
    description="LangChain API Server",
)

model1 = Ollama(model="Gemma3:4b")
model2 = Ollama(model="Gemma3:1b")


prompt1 = ChatPromptTemplate.from_template("Write me a code in Python on {topic} and i just want code no explanation needed")
prompt2 = ChatPromptTemplate.from_template("Write me a code in c++ on {topic} and i just want code no explanation needed")

add_routes(
    app,
    prompt1|model1,
    path="/python"
)

add_routes(
    app,
    prompt2|model2,
    path="/cpp"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

load_dotenv(dotenv_path=".env")
os.environ ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")