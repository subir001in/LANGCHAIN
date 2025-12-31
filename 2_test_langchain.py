import os
from func_utils import load_api_key_from_file
from langchain.chat_models import init_chat_model  


# Initialize the OpenAI client with your API key
api_key = load_api_key_from_file("OPENAI_API_KEY.txt")
if not api_key:
    raise RuntimeError(
        "OpenAI API key not found. Set the OPENAI_AP_KEY environment key or put in the file"
    )

print(api_key)
llm_client = init_chat_model(model_provider="openai", model="gpt-4o-mini", api_key=api_key)

# Define a simple prompt for the agent 
prompt = "You are a helpful assistant. What can you do?"

#Send the prompt to the language model and retrieve the response
response = llm_client.invoke(prompt, config={"max_tokens": 16})
print("Response from the language model:", response.content)