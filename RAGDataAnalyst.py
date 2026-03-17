from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpoint
import os 
os.environ['HF_Token']  =  ""
loader  = CSVLoader(file_path  = 'synthetic_sales_data.csv')
documents  = loader.load()
#splitter 
text_splitter  = CharacterTextSplitter(chunk_size  = 500)

docs = text_splitter.split_documents(documents)
#embeddings 
embeddings  = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#vector databases 
vector_store  = FAISS.from_documents(docs,embeddings)

#retriver 
retriever  = vector_store.as_retriever()

#llm 
llm = HuggingFaceEndpoint(repo_id='openai/gpt-oss-20b',max_new_tokens=200)

 
#query 
query = "which one city has the most highest sales"

retrieved_docs  = retriever._get_relevant_documents(query)

context = "\n".join([doc.page_content for doc in retrieved_docs])

prompt= f""" answer the question using following context 
context:{context}
query : {query}
"""
res  = llm.invoke(prompt)

print(res)
