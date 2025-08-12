# langchain-faiss-rag

# LangChain + FAISS + OpenAI Embeddings Example

This project demonstrates how to:
1. Load text from a webpage.
2. Split it into smaller chunks.
3. Convert the chunks into vector embeddings using OpenAI.
4. Store and search these embeddings in a FAISS vector database.
5. Use a Retrieval-Augmented Generation (RAG) chain to answer questions from the webpage.

---

## 🚀 Features
- Web scraping via **LangChain WebBaseLoader**
- **RecursiveCharacterTextSplitter** for chunking
- **OpenAIEmbeddings** for semantic vectors
- **FAISS** for similarity search
- Retrieval-Augmented Generation with **ChatOpenAI**

---

## 📦 Installation


git clone https://github.com/YOUR_USERNAME/langchain_faiss_example.git
cd langchain_faiss_example 
pip install -r requirements.txt
🔑 Setup
Create a .env file in the root folder:


OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here   # Optional
LANGCHAIN_PROJECT=LangChain_FAISS_Demo          # Optional
Get your OpenAI API key from:
https://platform.openai.com/account/api-keys

▶️ Run
python main.py
📌 Example Output

🔹 Loading website content...
🔹 Splitting documents into chunks...
🔹 Creating embeddings...
🔹 Storing vectors in FAISS...
🔹 Initializing LLM...

❓ Question: What are the two usage limits in LangSmith?

💡 Answer:
LangSmith has two usage limits: total traces and extended traces, which correspond to the metrics shown in the usage graph.
🛠 Tech Stack
LangChain

OpenAI

FAISS

📄 License
MIT License


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


![Logo](https://static.wixstatic.com/media/1f98e0_e86e5bc74d254fcc919217c0e3121efe~mv2.jpg/v1/fill/w_600,h_315,al_c/1f98e0_e86e5bc74d254fcc919217c0e3121efe~mv2.jpg)

