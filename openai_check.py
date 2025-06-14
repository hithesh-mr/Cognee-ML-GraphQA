# This code to check if the OpenAI API key is valid

import os
from openai import OpenAI
from dotenv import load_dotenv

def check_openai_api_key():
    """
    Checks if the OpenAI API key is valid by making a simple API call.
    Assumes the API key is stored in a .env file.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found.")
        print("Please create a .env file and add your API key to it.")
        return False

    try:
        client = OpenAI(api_key=api_key)
        client.models.list()
        print("OpenAI API key is valid!")
        return True
    except Exception as e:
        print(f"Invalid OpenAI API key. Error: {e}")
        return False

if __name__ == "__main__":
    check_openai_api_key()
