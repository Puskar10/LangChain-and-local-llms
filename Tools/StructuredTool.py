from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# 1. Define input schema
class MultipleInput(BaseModel):
    a: int = Field(
        ...,
        description="First number to add"
    )

    b: int = Field(
        ...,
        description="Second number to add"
    )


# 2. Define function
def add_func(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# 3. Create StructuredTool
add_tool = StructuredTool.from_function(
    func=add_func,
    name="add",
    description="Add two numbers",
    args_schema=MultipleInput
)


# 4. Execute tool
result = add_tool.invoke({
    "a": 3,
    "b": 3
})


# 5. Display information
print("Result:", result)
print("Name:", add_tool.name)
print("Description:", add_tool.description)
print("Arguments:", add_tool.args)
