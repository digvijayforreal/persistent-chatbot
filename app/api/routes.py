from fastapi import APIRouter
from app.schemas.models import ChatRequest
from app.services.chatbot import chat
from app.services.memory_service import get_chat_history
from app.services.memory_service import list_saved_sessions
router = APIRouter()


@router.post("/chat")
def send_message(request: ChatRequest):
    answer = chat(
        question=request.message,
        session_id=request.session_id
    )

    return {
        "session_id": request.session_id,
        "response": answer
    }


@router.get("/sessions/{session_id}/messages")
def get_messages(session_id: str):
    history = get_chat_history(session_id)

    messages = []

    for message in history.messages:
        messages.append({
            "role": message.type,
            "content": message.content
        })

    return {
        "session_id": session_id,
        "messages": messages
    }




@router.get("/sessions")
def get_sessions():
    return {
        "sessions": list_saved_sessions()
    }