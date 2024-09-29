from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_google_vertexai import ChatVertexAI
from langchain_mistralai import ChatMistralAI

import streamlit as st
import os
from dotenv import load_dotenv

# from google.cloud import aiplatform

# aiplatform.init(project="project_id")

os.environ["MISTRAL_API_KEY"] = "MISTRAL_API_KEY"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="LANGCHAIN_API_KEY"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
# model = ChatVertexAI(model="gemini-1.5-flash",
#                     project_id = 'gen-lang-client-0401673135')

model = ChatMistralAI(model="mistral-large-latest")
output_parser=StrOutputParser()
chain=prompt|model|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
