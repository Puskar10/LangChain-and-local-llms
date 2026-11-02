from tinyllama_model import load_tinyllama

llm = load_tinyllama()

print("TinyChat AI started! Type 'exit' to quit.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = llm.invoke(question)

    print("\nTinyLlama:", response)