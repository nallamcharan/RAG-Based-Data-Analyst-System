## 📊 RAG-Based Data Analyst System
## 🎯 Objective

The objective of this project is to build a Retrieval-Augmented Generation (RAG) based system that can analyze structured CSV data and answer user queries in natural language.

This system acts like a data analyst assistant, helping users extract insights such as trends, comparisons, and summaries without writing SQL or complex code.

## 🚀 Approach

The system follows a RAG pipeline, combining retrieval and generation:

Convert CSV data into text format

Split text into smaller chunks

Transform chunks into embeddings (vector representation)

Store embeddings in a vector database (FAISS)

Retrieve relevant data based on user query

Use an LLM to generate answers from retrieved context

## ⚙️ End-to-End Workflow
Step 1: Load Data

Load CSV file using LangChain's CSVLoader

Convert structured data into documents

Step 2: Text Splitting

Split large documents into smaller chunks

Helps improve retrieval accuracy

Step 3: Generate Embeddings

Use Hugging Face embedding model

Convert text chunks into numerical vectors

Step 4: Store in Vector Database

Store embeddings in FAISS

Enables fast similarity search

Step 5: Retrieval

Convert user query into embedding

Retrieve most relevant chunks from FAISS

Step 6: Context Creation

Combine retrieved chunks into a single context

Step 7: LLM Response Generation

Pass context + query to LLM

Generate final answer

## 🛠️ Tech Stack

Python

LangChain

Hugging Face (Embeddings + LLM)

FAISS

📁 Dataset

synthetic_sales_data.csv

Contains sales-related information for analysis

▶️ How to Run

Install required libraries
pip install langchain langchain-community langchain-huggingface faiss-cpu

Set your Hugging Face API key
export HF_Token=your_api_key (Linux/Mac)
set HF_Token=your_api_key (Windows)

Run the script
python app.py

💡 Example Query

Which city has the highest sales?

## 📊 Output

The system retrieves relevant data from the dataset and generates a natural language answer using the LLM.

🔥 Key Features

Natural language querying on CSV data
