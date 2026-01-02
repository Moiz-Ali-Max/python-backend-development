conversation_history = []
max_mesg_memory = 10


def add_message(role: str, content: str):
    conversation_history.append({
        "role": role,
        "content": content
    })

    if len(conversation_history) > max_mesg_memory:
        conversation_history.pop(0)


def get_conversation_text():
    context = ""
    for msg in conversation_history:
        if msg["role"] == "user":
            context += f"User: {msg['content']}\n"
        else:
            context += f"Assistant: {msg['content']}\n"
    return context


def get_all_messages():
    return conversation_history


def clear_conversation():
    conversation_history.clear()
