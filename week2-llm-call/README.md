# Week 2 LLM Client

A Python client that supports Gemini and a local Ollama model through a shared
provider interface.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. For Gemini, copy `.env.example` to `.env` and set `GEMINI_API_KEY`.
4. For Ollama, install Ollama and make sure the `llama3.2` model is available:

   ```powershell
   ollama pull llama3.2
   ```

5. Run the client:

   ```powershell
   python main.py
   ```

Choose `gemini` or `ollama` when prompted. Run the unit tests with:

```powershell
python -m unittest -v
```

Do not commit `.env` or share your API key.
