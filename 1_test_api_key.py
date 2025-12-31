from openai import OpenAI
import os


##FUNCTION TO LOAD API KEY FROM A FILE
def load_api_key_from_file(path: str) -> str | None:
    '''
    FUNCTION TO LOAD API KEY FROM A FILE
    '''
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # try to find token starting with sk-
            for part in content.split():
                print(part)
                if part.startswith("sk-"):
                    return part
            return content or None
    except FileNotFoundError:
        return None


#api_key = os.environ.get("OPENAI_API_KEY")
api_key = load_api_key_from_file("OPENAI_API_KEY.txt")

if not api_key:
    raise RuntimeError(
        "OpenAI API key not found. Set the OPENAI_API_KEY environment variable or put the key in OPENAI_API_KEY.txt"
    )

#print(api_key)
client = OpenAI(api_key=api_key)
print("Using OpenAI client — redacted key prefix:", api_key[:8] + "...")

# Test the API connection with a small responses request
response = client.responses.create(
    model="gpt-4o-mini",  # use a generally available model; change if needed
    input="Where is Taj Mahal ?",
    max_output_tokens=16,
)

print(f"Response received: {response.output_text}")