# Get the API key from the local ENV
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Grab the Gemini libs
from google import genai
from google.genai import types
client = genai.Client(api_key=api_key)

import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("prompt", type=str, help="Prompt for the AI agent")
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        print("must enter a prompt")
        sys.exit(1)

    prompt_text = args.prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt_text)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if args.verbose:
        print(f"User prompt: {prompt_text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

if __name__ == "__main__":
    main()
