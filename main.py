import os
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Set environment variables (LangSmith tracing optional)
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "")

# 3. Import required LangChain components
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

# -------------------------
# STEP 1: Load Data from Website
# -------------------------
print("🔹 Loading website content...")
loader = WebBaseLoader("https://docs.smith.langchain.com/tutorials/Administrators/manage_spend")
docs = loader.load()

# -------------------------
# STEP 2: Split Documents into Chunks
# -------------------------
print("🔹 Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(docs)

# -------------------------
# STEP 3: Create Embeddings
# -------------------------
print("🔹 Creating embeddings...")
embeddings = OpenAIEmbeddings()

# -------------------------
# STEP 4: Store in FAISS Vector DB
# -------------------------
print("🔹 Storing vectors in FAISS...")
vectorstoredb = FAISS.from_documents(documents, embeddings)

# -------------------------
# STEP 5: Initialize LLM
# -------------------------
print("🔹 Initializing LLM...")
llm = ChatOpenAI(model="gpt-4o")

# -------------------------
# STEP 6: Create Document Chain
# -------------------------
prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context:
<context>
{context}
</context>
""")
document_chain = create_stuff_documents_chain(llm, prompt)

# -------------------------
# STEP 7: Create Retrieval Chain
# -------------------------
retriever = vectorstoredb.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# -------------------------
# STEP 8: Ask a Question
# -------------------------
question = "What are the two usage limits in LangSmith?"
print(f"\n❓ Question: {question}\n")

response = retrieval_chain.invoke({"input": question})

print("💡 Answer:")
print(response["answer"])
