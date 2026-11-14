# 🦜 LangChain & Local LLMs – Learning Repository

Welcome to my **LangChain and Local LLMs Learning Repository**! 🚀

This repository documents my hands-on journey into Generative AI, LangChain, and running Large Language Models (LLMs) locally. It contains practical examples, experiments, code implementations, and projects that help me understand how to build AI-powered applications using both cloud-based and locally hosted models.

My goal is to learn how LLMs work, integrate them with LangChain, experiment with different models, and eventually build intelligent AI applications.

---

## 🎯 Learning Objectives

- Understand the fundamentals of Large Language Models (LLMs).
- Learn LangChain and its core components.
- Work with local LLMs without depending entirely on cloud APIs.
- Integrate Hugging Face models with LangChain.
- Understand Prompt Templates and Output Parsers.
- Generate structured and unstructured outputs.
- Learn LangChain Expression Language (LCEL).
- Implement sequential and parallel chains.
- Explore document loading, splitting, and embeddings.
- Build Retrieval-Augmented Generation (RAG) applications.
- Develop practical Generative AI projects.

---

## 🛠️ Technologies & Tools

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| LangChain | LLM application development |
| Hugging Face | Access and run pretrained models |
| Ollama | Run LLMs locally |
| TinyLlama | Lightweight local language model |
| Gemma | Experiment with open models |
| Qwen | Experiment with local LLMs |
| Transformers | Load and run pretrained models |
| PyTorch | Deep learning framework |
| Streamlit | Build interactive AI applications |
| dotenv | Manage environment variables |
| Git & GitHub | Version control |

---

## 📚 Learning Roadmap

### 1. LangChain Fundamentals
- Introduction to LangChain
- Chat Models and LLMs
- Prompt Templates
- Chat Prompt Templates
- Output Parsers
- String Output Parser
- Structured Output Parser
- Response Schemas

### 2. LangChain Runnables & Chains
- LangChain Expression Language (LCEL)
- RunnableSequence
- RunnableParallel
- RunnablePassthrough
- RunnableLambda
- Sequential Chains
- Parallel Execution

### 3. Hugging Face Integration
- Hugging Face Models
- HuggingFaceEndpoint
- ChatHuggingFace
- Transformers Pipeline
- Loading pretrained models
- Text generation using local models

### 4. Local LLMs
- Introduction to Local LLMs
- Installing Ollama
- Running models locally
- TinyLlama 1.1B
- Gemma 2 2B
- Qwen models
- Local model inference
- Model quantization and optimization

### 5. Document Processing & RAG
- Document Loaders
- Text Loaders
- WebBaseLoader
- PDF Document Loader
- Text Splitters
- Text Embeddings
- Vector Databases
- Similarity Search
- Retrieval-Augmented Generation (RAG)

### 6. AI Application Development
- Building AI chatbots
- Integrating local LLMs with Streamlit
- Structured data extraction
- Document-based question answering
- Conversational AI
- Building practical AI assistants

---

## 📂 Repository Structure

```text
LangChain-and-local-llms/
│
├── models/
│   ├── TinyLlama/
│   └── ...
│
├── prompt-templates/
│
├── output-parsers/
│
├── runnables/
│
├── huggingface/
│
├── ollama/
│
├── document-loader/
│
├── text-splitters/
│
├── embeddings/
│
├── vector-databases/
│
├── rag/
│
├── projects/
│
├── .env.example
├── requirements.txt
└── README.md
```

*Note: The structure will evolve as I continue learning and adding new implementations.*

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Puskar10/LangChain-and-local-llms.git

cd LangChain-and-local-llms
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory.

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Only configure the API keys required for the examples you want to run. Never commit your actual `.env` file.

### 5. Run Local Models

For Ollama-based experiments, install Ollama and download a model:

```bash
ollama pull qwen3.5:4b
```

Run the model:

```bash
ollama run qwen3.5:4b
```

---

## 🧪 Practical Experiments

Some of the experiments covered in this repository include:

- Creating prompts using PromptTemplate.
- Generating responses using local LLMs.
- Parsing model responses into structured JSON.
- Comparing cloud-based and local models.
- Running multiple LLMs using RunnableParallel.
- Loading documents from websites.
- Building document-based AI applications.
- Creating a simple local AI chatbot using TinyLlama and Streamlit.

---

## 💻 Development Environment

My local development setup:

- **OS:** Windows
- **Language:** Python
- **RAM:** 12 GB
- **GPU:** NVIDIA RTX 2050 (4 GB VRAM)
- **IDE:** Visual Studio Code
- **Environment:** Python Virtual Environment

I focus on lightweight models and resource-efficient implementations that can run on consumer hardware.

---

## 📈 Learning Progress

- [x] Python and LLM environment setup
- [x] LangChain fundamentals
- [x] Prompt Templates
- [x] String Output Parser
- [x] Structured Output Parser
- [x] Hugging Face integration
- [x] TinyLlama local model setup
- [x] Streamlit local chatbot experiment
- [x] RunnableParallel experiments
- [x] Document loading experiments
- [ ] Advanced LCEL
- [ ] Text splitting and embeddings
- [ ] Vector databases
- [ ] RAG implementation
- [ ] Advanced local LLM optimization
- [ ] AI agent development

*Progress is updated as I complete new experiments.*

---

## 🎯 Long-Term Goal

My long-term goal is to become proficient in Generative AI and build practical AI applications using LangChain and locally hosted LLMs.

I also aim to develop a lightweight **Local AI Assistant** capable of:

- Understanding natural language.
- Processing voice input using Speech-to-Text.
- Generating voice responses using Text-to-Speech.
- Performing computer-related tasks.
- Interacting with local files and applications.
- Running efficiently without requiring expensive cloud infrastructure.

---

## 👨‍💻 About Me

**Puskar Shaw**

Diploma Computer Science & Engineering Student | Full Stack Developer | Generative AI Enthusiast

I enjoy exploring new technologies, building real-world projects, and learning how AI can solve practical problems.

- GitHub: [@Puskar10](https://github.com/Puskar10)
- Portfolio: [puskar-shaw-portfolio.vercel.app](https://puskar-shaw-portfolio.vercel.app/)
- LinkedIn: [Connect with me](https://www.linkedin.com/)

---

⭐ If you find this repository useful, consider giving it a star!

**Learning by building. Experimenting with AI. Growing every day. 🚀**
