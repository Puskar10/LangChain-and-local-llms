
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# Configure search wrapper
wrapper = DuckDuckGoSearchAPIWrapper(
    backend="auto",
    max_results=5
)

# Create search tool
search_tool = DuckDuckGoSearchRun(
    api_wrapper=wrapper
)

# Execute search
try:
    results = search_tool.invoke({
        "query": "What is the capital of France?"
    })

    print("Search Results:")
    print(results)

except Exception as e:
    print("Error:", repr(e))
