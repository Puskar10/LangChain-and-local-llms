
from tinyllama_model import load_tinyllama

llm = load_tinyllama()

print("\nTinyChat AI started!")
print("Type 'exit' to quit.\n")

SYSTEM_PROMPT = """
You are TinyChat, a helpful AI assistant.
Answer the user's question directly.
Use simple English.
Give accurate and relevant information.
If you do not know something, say so.
Do not invent facts.
"""

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # TinyLlama chat format
    prompt = f"""<|system|>
{SYSTEM_PROMPT}</s>
<|user|>
{question}</s>
<|assistant|>
"""

    try:
        response = llm.invoke(prompt)

        print("\nTinyLlama:", response.strip(), "\n")

    except Exception as e:
        print("Error:", e)
