# ✦ Persistent AI Chatbot

### An AI assistant that remembers your conversations.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-LLM%20Framework-green" />
  <img src="https://img.shields.io/badge/Groq-AI%20Inference-orange" />
  <img src="https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb&logoColor=white" />
</p>

<p align="center">
  <b>Chat naturally. Save conversations. Continue where you left off.</b>
</p>

---

## 📸 Project Preview

<!-- Add your actual project screenshots to the screenshots/ folder -->

<p align="center">
  <img src="screenshots/chat-interface.png" width="90%" alt="Persistent Chatbot Interface" />
</p>

<p align="center">
  <i>Main chatbot interface with saved conversations and AI responses.</i>
</p>

<p align="center">
  <img src="screenshots/conversation-history.png" width="90%" alt="Saved Conversation History" />
</p>

<p align="center">
  <i>Previously saved conversations.</i>
</p>

---

## 🚀 About The Project

**Persistent AI Chatbot** is an AI-powered conversational application designed to maintain conversation history across multiple sessions.

Unlike a basic chatbot that loses its context when a session ends, this application stores messages in MongoDB Atlas and retrieves previous conversation history using session IDs.

The chatbot uses LangChain's message history management to provide contextual responses through Groq-powered language models.

The goal is to create an AI assistant that can remember previous interactions and allow users to continue their conversations even after restarting the application.

### ✨ Key Features

- 💬 **AI-Powered Conversations** — Interact with an LLM using natural language.
- 🧠 **Persistent Chat History** — Store conversations in MongoDB Atlas.
- 🔄 **Session-Based Memory** — Maintain separate conversation histories using session IDs.
- 📂 **Saved Conversations** — Retrieve previously created chat sessions.
- ⚡ **Context-Aware Responses** — Use previous messages when generating new responses.
- 🗄️ **MongoDB Integration** — Persist chat messages beyond application restarts.
- 🌐 **Web Interface** — Simple frontend for interacting with the chatbot.
- 🔌 **REST API** — FastAPI endpoints for sending messages and retrieving history.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12+ | Core programming language |
| FastAPI | Backend API framework |
| LangChain | LLM orchestration and chat history |
| ChatGroq | Language model integration |
| MongoDB Atlas | Persistent conversation storage |
| Uvicorn | ASGI server |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend interactions |
| uv | Python dependency management |

---

## 🏗️ System Architecture

```text
                 USER
                   |
                   v
          FRONTEND INTERFACE
             HTML / CSS / JS
                   |
                   v
             FASTAPI SERVER
                   |
                   v
             CHAT API ROUTE
                   |
                   v
          LANGCHAIN CHATBOT
                   |
          +--------+--------+
          |                 |
          v                 v
      GROQ LLM         CHAT HISTORY
          |                 |
          v                 v
      AI RESPONSE      MONGODB ATLAS
                            |
                       Session ID
                            |
                      Saved Messages
```

### 🧠 How Persistent Memory Works

1. A user starts a conversation with a session ID.
2. The message is sent to the FastAPI backend.
3. LangChain retrieves the conversation history associated with that session ID.
4. The previous messages and new question are passed to the Groq language model.
5. The AI generates a contextual response.
6. LangChain stores the new interaction in MongoDB Atlas.
7. When the user returns to the same session, the previous history can be retrieved.

**Storage Configuration:**
- Database: `persistent_chatbot_db`
- Collection: `chat_history`
- History size: 20 messages per session retrieval configuration.

---

## 📁 Project Structure

```text
persistent-chatbot/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── schemas/
│   │   └── models.py
│   │
│   ├── services/
│   │   ├── chatbot.py
│   │   └── memory_service.py
│   │
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── scripts/
│
├── src/
│   └── persistent_chatbot/
│
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Getting Started

Follow these instructions to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/digvijayforreal/persistent-chatbot.git
```

```bash
cd persistent-chatbot
```

### 2. Install Dependencies

This project uses `uv` for Python package management.

Install uv if you haven't already:

```bash
pip install uv
```

Install project dependencies:

```bash
uv sync
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
MONGODB_URI=your_mongodb_connection_string
```

**Get your API credentials:**

- Groq API: https://console.groq.com/keys
- MongoDB Atlas: https://www.mongodb.com/products/platform/atlas-database

Make sure your MongoDB Atlas cluster is running and your connection string is configured correctly.

### 4. Run the Application

Start the FastAPI development server:

```bash
uv run uvicorn app.main:app --reload
```

### 5. Open the Application

| Service | URL |
|---|---|
| Chatbot Interface | http://127.0.0.1:8000 |
| FastAPI Swagger Docs | http://127.0.0.1:8000/docs |
| ReDoc API Docs | http://127.0.0.1:8000/redoc |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/chat` | Send a message to the chatbot |
| GET | `/sessions` | Retrieve saved conversation sessions |
| GET | `/sessions/{session_id}/messages` | Retrieve messages from a specific session |

### Example: Send a Chat Message

**POST** `/chat`

Request:

```json
{
  "session_id": "session_001",
  "message": "Hello, who are you?"
}
```

Response:

```json
{
  "session_id": "session_001",
  "response": "Hello! I'm your AI assistant. How can I help you?"
}
```

---

## 🔐 Environment & Security

- Keep API keys and database credentials inside `.env`.
- Never commit `.env` to GitHub.
- Configure MongoDB Atlas network access appropriately.
- Use `.gitignore` to exclude sensitive files and local environments.

---

## 🔮 Future Improvements

- [ ] User authentication and personal chat accounts.
- [ ] Rename and delete conversations.
- [ ] Conversation search functionality.
- [ ] Better long-term memory and summarization.
- [ ] Streaming AI responses.
- [ ] Export conversations.
- [ ] Deployment with a cloud hosting provider.

---

## 🎯 Learning Outcomes

Through this project, I explored:

- Building REST APIs with FastAPI.
- Integrating LLMs using LangChain.
- Working with Groq-powered language models.
- Implementing persistent conversation history.
- Managing session-based memory.
- Connecting MongoDB Atlas with Python applications.
- Developing a frontend for an AI-powered application.

---

## 👨‍💻 Author

**Digvijay Mali**

AI/ML Engineer | Python Developer | Generative AI Enthusiast

- GitHub: https://github.com/digvijayforreal

---

<p align="center">
  <b>Built with Python, LangChain, Groq & MongoDB.</b>
  <br/>
  <i>Making AI conversations persistent, one message at a time. ✦</i>
</p>