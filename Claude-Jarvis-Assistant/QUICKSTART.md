# Quick Start Guide

Get your Claude-powered Jarvis running in 5 minutes!

## Step 1: Get Your API Key

1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy it (you won't see it again!)

## Step 2: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

**Having issues with PyAudio?**
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **macOS**: `brew install portaudio`
- **Windows**: Download wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

## Step 3: Configure API Key

**Option A - Quick (for testing):**
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

**Option B - Permanent (recommended):**
```bash
# Create .env file
cp .env.example .env

# Edit .env and add your key
nano .env  # or use your favorite editor
```

Then add this to the top of `claude_jarvis.py` (after imports):
```python
from dotenv import load_dotenv
load_dotenv()
```

## Step 4: Run Jarvis!

```bash
python claude_jarvis.py
```

## Step 5: Try It Out!

Say one of these:
- "What time is it?"
- "Open YouTube"
- "Tell me about Python programming"
- "Create a file called test.txt with hello world"
- "Take a screenshot"
- "Goodbye" (to exit)

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
- Make sure you set the environment variable or created .env file
- If using .env, add `from dotenv import load_dotenv; load_dotenv()` to the script

### "No module named 'pyaudio'"
- Install system dependencies (see Step 2)
- Try: `pip install pyaudio` separately

### "Could not understand audio"
- Check your microphone is working
- Ensure you have internet (speech recognition needs it)
- Speak clearly and close to the microphone
- Reduce background noise

### "Speech recognition error"
- Make sure you have internet connection
- Google Speech API requires internet access

## Next Steps

- Read the full [README.md](README.md) for advanced features
- Customize the system prompt to change Jarvis's personality
- Add your own tools for custom capabilities
- Experiment with different Claude models

---

**Need help?** Check the full README.md or open an issue!
