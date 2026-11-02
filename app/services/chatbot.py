import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

from app.services.memory_service import get_chat_history

load_dotenv()


llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=1000
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Answer questions clearly and accurately.
Use previous conversation messages when relevant.
Do not invent missing memories.
Keep responses natural and concise."""
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

chatbot = RunnableWithMessageHistory(
    chain,
    get_chat_history,
    input_messages_key="question",
    history_messages_key="history"
)


def chat(question: str, session_id: str) -> str:

    return chatbot.invoke(
        {"question": question},
        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )
    