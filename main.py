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
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("prompt", type=str, help="Prompt for the AI agent")
    args = parser.parse_args()

    if not len(sys.argv) > 1:
        print("must enter a prompt")
        sys.exit(1)

    # Config Data
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """
    model_name = "gemini-2.0-flash-001"
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    prompt_text = args.prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt_text)])
    ]

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions])
    )

    if args.verbose:
        print(f"User prompt: {prompt_text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls != None:
        for fcall in response.function_calls:
            print(f"Calling function: {fcall.name}({fcall.args})")
    else:
        print(response.text)

if __name__ == "__main__":
    main()
