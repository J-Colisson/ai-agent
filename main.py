import os
import argparse
import json
import sys
from dotenv import load_dotenv
from prompts import system_prompt
from functions.call_function import *


def main() -> None:
        
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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    iteration = 0
    for _ in range(20):
        iteration += 1
        completion = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        )


        if completion.usage == None :
            raise RuntimeError("no completion")
        message = completion.choices[0].message
        messages.append(message)
        if args.verbose :
            print("User prompt: " + args.user_prompt)
            print("Prompt tokens: "+ str(completion.usage.prompt_tokens))
            print("Response tokens: "+ str(completion.usage.completion_tokens))
        if completion.choices[0].message.tool_calls :
            for tool_call in completion.choices[0].message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call)
                messages.append(result_message)
                if args.verbose :
                    print(f"-> {result_message['content']}")
                continue
        if completion.choices[0].message.content :       
            print("Final response: \n"+ completion.choices[0].message.content)
            break
        if iteration == 20:
            exit(1)

if __name__ == "__main__":
    main()

# ----------------------------



