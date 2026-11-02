from app.services.chatbot import chat

SESSION_ID = "chat_test_001"

print("Persistent Chatbot")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    try:
        answer = chat(
            question=question,
            session_id=SESSION_ID
        )

        print("\nAI:", answer, "\n")

    except Exception as e:
        print("Error:", e)