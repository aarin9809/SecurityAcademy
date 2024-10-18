
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_community.document_loaders import PyMuPDFLoader

from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union

from langchain.text_splitter import RecursiveCharacterTextSplitter

llm = ChatOllama(model="Llama-3-Open-Ko-8B-Q4_K_S.gguf:latest")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, professional assistant named AIBot. Introduce yourself first, and answer the questions."),
    MessagesPlaceholder(variable_name='messages1'),    
])

chain = prompt | llm | StrOutputParser()

#chain.invoke({"input":"What is stock?"})