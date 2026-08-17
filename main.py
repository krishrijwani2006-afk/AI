import os
import argparse
def main():
    print("Hello from ai!")

    
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set.")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    response = client.chat.completions.create(model="openrouter/free", messages = [
    {
        "role": "user",
        "content": args.user_prompt,
    }
    ])

    if response.usage:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("No usage information returned in the response.")

    print(response.choices[0].message.content)
if __name__ == "__main__":
    main()
