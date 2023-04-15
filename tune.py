import os
import openai
from llama_index import download_loader, GPTSimpleVectorIndex, Document, SimpleDirectoryReader
from pathlib import Path

JSONReader = download_loader("JSONReader")

def chunk_text(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def create_chunked_documents(documents, chunk_size=2048):
    chunked_documents = []
    for doc in documents:
        content = doc.get('content')
        if content:
            chunks = chunk_text(content, chunk_size)
            for i, chunk in enumerate(chunks):
                chunked_documents.append(
                    Document(title=f"{doc.get('title')}_{i}", content=chunk)
                )
    return chunked_documents

loader = JSONReader()
documents = loader.load_data(Path('./scraped_data.json'))

with open('openaiapikey.txt', 'r') as f:
    openai.api_key = f.read().strip()
    os.environ['OPENAI_API_KEY'] = openai.api_key

index = GPTSimpleVectorIndex.from_documents(documents)

index.save_to_disk('./data/playoffs_index.json')



