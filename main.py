import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None :
    raise Exception("API Key not found")

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

completion = client.chat.completions.create(
  model="openrouter/free",
  messages=[
    {"role": "user", "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."},
  ]
  
)



if completion.usage == None :
    raise RuntimeError("no completion")
print("User prompt: ")
print("Prompt tokens: "+ str(completion.usage.prompt_tokens))
print("Response tokens: "+ str(completion.usage.completion_tokens))
print("Response: "+ completion.choices[0].message.content)



# ----------------------------


def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
