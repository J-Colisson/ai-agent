import os
import argparse
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

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt},
]

completion = client.chat.completions.create(
  model="openrouter/free",
  messages=messages
)



if completion.usage == None :
    raise RuntimeError("no completion")
if args.verbose :
    print("User prompt: " + args.user_prompt)
    print("Prompt tokens: "+ str(completion.usage.prompt_tokens))
    print("Response tokens: "+ str(completion.usage.completion_tokens))
print("Response: "+ completion.choices[0].message.content)



# ----------------------------


def main():
    


if __name__ == "__main__":
    main()
