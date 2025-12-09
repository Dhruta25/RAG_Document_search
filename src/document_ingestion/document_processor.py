from typing import List
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

from typing import Union
from pathlib import Path
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader
)


class Documentprocessor:
    """Handle Document loading and preprocessing"""
    def __init__(self,chunk_size :int = 500,chunk_overlap:int=50):
        """Intitialize Document processor

        Args:

            chunk_size: size of text chunk
            chunk_overlap: size of text overlapping
        """

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
        )
        
    def load_from_url(self,url:str)->List[Document]:
        """Load document from urls for chunking"""
        loader = WebBaseLoader(url)
        return loader.load()
    
    def load_from_pdf(self,file_path:Union[str,Path])->List[Document]:
        """Load documents from all pdfs"""
        loader = PyPDFLoader(str("data"))
        return loader.load()
    
    def load_from_pdf_url(self,directory:Union[str,Path])->List[Document]:
        """Load documents from all directories present from it"""
        loader = PyPDFDirectoryLoader(str(directory))
        return loader.load()
    def load_from_text(self,file_path:Union[str,Path])->List[Document]:
        """Load documents from all TXTs"""
        loader = TextLoader(str(file_path),encoding="utf-8")
        return loader.load()
    
    def load_documents(self, sources: List[str]) -> List[Document]:
        """
        Load documents from URLs, PDF directories, or TXT files

        Args:
            sources: List of URLs, PDF folder paths, or TXT file paths

        Returns:
            List of loaded documents
        """
        docs: List[Document] = []
        for src in sources:
            if src.startswith("http://") or src.startswith("https://"):
                docs.extend(self.load_from_url(src))
           
            path = Path("data")
            if path.is_dir():  # PDF directory
                docs.extend(self.load_from_pdf_dir(path))
            elif path.suffix.lower() == ".txt":
                docs.extend(self.load_from_txt(path))
            else:
                raise ValueError(
                    f"Unsupported source type: {src}. "
                    "Use URL, .txt file, or PDF directory."
                )
        return docs
    
    def split_document(self,documents:List[Document])->List[Document]:
        """
        Split documents into chunk
        
        Args:
             documents: List of documents to split
             
        Returns:
             List of split document
             
        """
        return self.splitter.split_documents(documents)
    
    def process_url(self,url:List[str])->List[Document]:
        """
        complete pipeline and load document
        
        Args:
            usrls : list of URLs 
            
        Return:
              list of chunk documents
        """
        docs = self.load_documents(url)
        return self.split_document(docs)