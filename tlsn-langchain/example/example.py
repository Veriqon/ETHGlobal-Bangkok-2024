import asyncio
import tlsn_langchain
import os
import json

from dotenv import load_dotenv
load_dotenv()

messages =[
   """{
        \"role\": \"user\",
        \"content\": \"hi im bob! and i live in sf\"
    }""",
    """{
        \"role\": \"assistant\",
        \"content\": \"Hi Bob! It's great to meet you. How can I assist you today?\"
    }""",
    """{
        \"role\": \"user\",
        \"content\": \"whats the weather where I live?\"
    }"""
]

tools = [
    """
        {
            \"type\": \"function\",
            \"function\": {
                \"name\": \"tavily_search_results_json\",
                \"description\": \"A search engine optimized for comprehensive, accurate, and trusted results. Useful for when you need to answer questions about current events. Input should be a search query.\",
                \"parameters\": {
                    \"properties\": {
                        \"query\": {
                            \"description\": \"search query to look up\",
                            \"type\": \"string\"
                        }
                    },
                    \"required\": [\"query\"],
                    \"type\": \"object\"
                }
            }
        }
    """
]

top_p = 0.85
temperature = 0.3
stream = False
url = "https://api.red-pill.ai/v1/chat/completions"



async def run_async():
    result = await tlsn_langchain.exec_async("gpt-4o", os.getenv("REDPILL_API_KEY"), messages, tools, top_p, temperature, stream, url)
    print("Async Response Code: ", result.api_response.status_code)
    print("Async Response Json: ", result.api_response.json())
    print("Async Response Proof Length: ", result.proof.replace("\n", "").replace(" ", ""))


def main():
    # Run the sync function
    print("Running the sync function")
    result = tlsn_langchain.exec("gpt-4o", os.getenv("REDPILL_API_KEY"), messages, tools, top_p, temperature, stream, url)
    print("Sync Response Code: ", result.api_response.status_code)
    print("Sync Response Json: ", result.api_response.json())
    print("Sync Response Proof Length: ", len(result.proof))

    # Run the async function
    print("Running the async function")
    asyncio.run(run_async())


if __name__ == "__main__":
    main()