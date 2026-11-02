from app.services.memory_service import get_chat_history

history = get_chat_history("test_session_001")

print("Saved messages:", len(history.messages))

history.add_user_message("My favorite language is Python.")

history.add_ai_message(
    "Python is your favorite programming language."
)

print("\nConversation history:")

for message in history.messages:
    print(message.type, ":", message.content)