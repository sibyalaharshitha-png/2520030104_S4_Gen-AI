
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send prompt to Gemini
print("Connecting to Gemini...")

try:
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input="What is Artificial Intelligence? Explain in simple words."
    )

    # Step 5: Display response
    print("\n========== LLM RESPONSE ==========")
    print(response.output_text)
    print("==================================")

except Exception as error:
    print("\nSomething went wrong:")
    print(error)
