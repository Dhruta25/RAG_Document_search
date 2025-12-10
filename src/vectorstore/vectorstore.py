"""vector store is for embedding and retrival"""
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.schema import Document


class vectorstore:
    def __init__(self):
        self.embedding = OpenAIEmbeddings()
        self.vectorstore = None
        self.retriever = None

    def create_retriever(self,documents: List[Document]):
        """create vector store from documents
           
           Args:
                convert document into embed
        """
        self.vectorstore = FAISS.from_documents(documents,self.embedding)
        self.retriever = self.vectorstore.as_retriever()

    def get_retriever(self):
        """get retriever instance 
          
            and 
           
           return retriever instances
           
        """
        if self.retriever is None:
            raise ValueError("vector store is not initialized . Call create_vector store first")
        return self.retriever
    
    def retrieve(self, query:str,k:int = 4)->List[Document]:
        """
        Retrieve relevel document according to query
        
         Args: 
              query: relevant ans for this quary will come
              k : number of similar answer will come 
              
         return:
            list of answers will come means k number
            
        """
        if self.retriever is None:
            return ValueError("vector store is not initialized.please initialized it")
        return self.retriever.invoke(query)
