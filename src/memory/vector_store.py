# vector_store.py
import os
from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# 可选：使用 OpenAI Embedding（如果未来换 Ollama embedding 也可以替换）
# from openai import OpenAI

class VectorStore:
    def __init__(self, persist_directory="vector_db"):
        """
        初始化向量数据库
        """
        os.makedirs(persist_directory, exist_ok=True)
        self.persist_directory = persist_directory

        # Chroma 配置
        self.client = Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=self.persist_directory
        ))

        # 使用默认 embedding function（可改成 Ollama）
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()

        # 建立 collection
        self.collection_name = "notes"
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_function
        )

    def add_document(self, doc_id: str, text: str, metadata: dict = None):
        """
        添加文档到向量数据库
        """
        if not text:
            return
        self.collection.add(
            documents=[text],
            metadatas=[metadata or {}],
            ids=[doc_id]
        )
        print(f"✅ 文档已加入向量数据库: {doc_id}")

    def query(self, query_text: str, n_results: int = 5):
        """
        语义检索
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results
