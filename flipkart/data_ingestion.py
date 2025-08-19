# Convert Flipkart Langchain Documents to Embeddings 
# using HF Embeddings Model and 
# store Embeddings in AstraDB Vector Store.

from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from flipkart.config import Config
from flipkart.data_convertor import DataConvertor

class DataIngestor:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )
        self.vector_store = AstraDBVectorStore(
            embedding=self.embedding_model,
            collection_name="db-flipkart-recommender-system",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )
    
    def ingest(self, load_existing=True):
        if load_existing == True:
            return self.vector_store
        
        docs = DataConvertor(Config.DATA_FILE_PATH).convert()

        self.vector_store.add_documents(docs)

        return self.vector_store
    
if __name__ == "__main__":
    ingestor = DataIngestor()
    ingestor.ingest(load_existing=False)
    print("Data ingestion completed successfully.")