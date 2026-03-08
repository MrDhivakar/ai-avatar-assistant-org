
import ollama
from database import get_memory

def reply(text):
    history = get_memory()
    memory_text = ""
    for h in history:
        memory_text += h + "\n"

    prompt = f"""Previous conversation:
{memory_text}

User: {text}
AI:"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]
