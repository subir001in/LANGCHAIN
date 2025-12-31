from openai import OpenAI
client = OpenAI()

print(client.api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one-sentence bedtime story about a unicorn.",
    max_output_tokens=16
)

print(response.output_text)