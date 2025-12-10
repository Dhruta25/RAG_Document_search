"""RAG state defination for langgraph"""

from typing import List
from pydantic import BaseModel
from langchain.schema import Document

class RAGState(BaseModel):
    question : str
    retrieved_docs : List[Document]=[]
    answer : str =""