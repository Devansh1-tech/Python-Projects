import os
from google import genai
# from google.genai.types import *   # for configs, if needed

def setup_gemini(api_key: str = "AIzaSyBOQmtnsWIGRNfVkDOTpz4dCvNTzGO1Vec"):
    """
    Initialize the Gemini client.
    You can either pass the API key explicitly, or use the
    environment variable GEMINI_API_KEY (or GOOGLE_API_KEY).
    """
    if api_key:
        client = genai.Client(api_key="AIzaSyBOQmtnsWIGRNfVkDOTpz4dCvNTzGO1Vec")
    else:
        # This picks up GEMINI_API_KEY or GOOGLE_API_KEY from env automatically
        client = genai.Client()
    return client

def chat_loop(client, model_name: str = "gemini-2.5-flash"):
    """
    A simple CLI chat loop using Gemini API models.
    """

    print("Gemini Chatbot\n(Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break

        try:
            # generate content
            response = client.models.generate_content(
                model=model_name,
                contents=user_input
            )
            # response.text contains the generated output
            print("Chatbot:", response.text.strip())
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    # Option A: set API key via environment variable
    #   export GEMINI_API_KEY="YOUR_API_KEY_HERE"
    #
    # Option B: hardcode for quick testing (not safe for production)
    API_KEY = "YOUR_GEMINI_API_KEY"   # replace with your key or set to None to use env var

    client = setup_gemini(api_key=API_KEY)
    chat_loop(client)
