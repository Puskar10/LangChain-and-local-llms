
from ddgs import DDGS

try:
    with DDGS() as ddgs:
        results = ddgs.text(
            "Python programming",
            max_results=5
        )

        print("Search results:")

        for result in results:
            print(result)

except Exception as e:
    print(type(e).__name__, str(e))
