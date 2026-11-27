from langchain_core.tools import tool


def mul(a,b):
    return a * b

def mul(a: int,b: int)-> int:
    return a * b

@tool
def mul(a: int, b: int) ->int:
    """Multiply two numbers."""
    return a * b

result = mul.invoke({"a": 3, "b": 4})

print(result)
print(mul.name)
print(mul.description)
print(mul.args)

print(mul.args_schema.model_json_schema())