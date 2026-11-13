# Week 1 LLM Call

A small Python project that calls the Gemini API and prints a response. It also
includes a script to list the Gemini models available to your API key.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set `GEMINI_API_KEY` to your Gemini API key.
4. Run the example:

   ```powershell
   python main.py
   ```

To list available models, run `python check_models.py`.

Do not commit `.env` or share your API key.
