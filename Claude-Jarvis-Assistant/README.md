# Claude-Powered Jarvis Voice Assistant

A desktop voice assistant powered by Anthropic's Claude AI with advanced tool-calling capabilities. Unlike traditional voice assistants, this Jarvis uses Claude's intelligence to understand context, execute complex tasks, and provide natural conversational responses.

## Overview

This voice assistant combines:
- **Voice Recognition**: Speak naturally to give commands
- **Claude AI Intelligence**: Advanced reasoning and task planning
- **Tool Execution**: Claude can actually execute tasks on your system
- **Voice Responses**: Hear Claude's responses spoken aloud

## Key Features

### Voice Commands
- Natural language processing through Claude
- Continuous conversation with context memory
- Time-aware greetings

### Claude-Powered Capabilities

Claude has access to the following tools and can use them to complete your requests:

1. **System Commands** - Execute shell commands and programs
2. **Web Browsing** - Open websites in your browser
3. **File Management** - Read, write, and list files/directories
4. **Time & Date** - Get current time and date information
5. **Screenshots** - Capture your screen
6. **Wikipedia Search** - Look up information
7. **Music Playback** - Play music from your Music directory
8. **And more!** - Claude can combine tools creatively to solve complex tasks

### Example Interactions

```
You: "What time is it?"
Jarvis: "It's 3:45 PM on Saturday, January 11th, 2026"

You: "Open YouTube and then tell me about artificial intelligence"
Jarvis: [Opens YouTube] "Artificial intelligence is the simulation of human intelligence..."

You: "Create a file called notes.txt with my grocery list: milk, eggs, bread"
Jarvis: [Creates file] "I've created notes.txt with your grocery list"

You: "What files are in my current directory?"
Jarvis: "You have the following files: [lists files]"

You: "Take a screenshot and tell me a fun fact about space"
Jarvis: [Takes screenshot] "Screenshot saved! Here's a fun fact about space..."
```

## Installation

### Prerequisites

1. **Python 3.8+**
2. **Anthropic API Key** - Get one from [Anthropic Console](https://console.anthropic.com/)
3. **Microphone** - For voice input
4. **Speakers/Headphones** - For voice output

### Platform-Specific Requirements

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
sudo apt-get install espeak ffmpeg libespeak1  # For text-to-speech
```

**macOS:**
```bash
brew install portaudio
```

**Windows:**
- PyAudio wheel may be needed - download from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### Setup Steps

1. **Clone or navigate to this directory:**
```bash
cd Claude-Jarvis-Assistant
```

2. **Create a virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up your Anthropic API key:**

**Option A - Environment Variable:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**Option B - .env file (recommended):**
Create a `.env` file in this directory:
```env
ANTHROPIC_API_KEY=your-api-key-here
```

Then modify `claude_jarvis.py` to load it:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Usage

### Starting Jarvis

```bash
python claude_jarvis.py
```

### Voice Commands

After starting, Jarvis will greet you and begin listening. Simply speak naturally:

- **General queries**: "What's the weather like?" (requires internet search tool)
- **File operations**: "Read the file notes.txt" or "Create a todo list file"
- **System tasks**: "List files in my downloads folder"
- **Web browsing**: "Open GitHub"
- **Information**: "Tell me about Python programming"
- **Screenshots**: "Take a screenshot"
- **Music**: "Play some music"
- **Exit**: Say "goodbye", "exit", or "quit"

### How It Works

1. **You speak** → Speech recognition converts to text
2. **Text sent to Claude** → Claude receives your request with available tools
3. **Claude plans & acts** → Claude uses tools as needed (open websites, read files, etc.)
4. **Response spoken** → Claude's response is converted to speech

### Tool Execution Flow

Claude can chain multiple tools together. For example:

```
You: "Create a file with today's date and then read it back to me"

Claude's process:
1. Uses get_current_time tool → Gets date
2. Uses write_file tool → Creates file with date
3. Uses read_file tool → Reads the file back
4. Responds: "I've created the file with today's date: [date]. The file contains..."
```

## Architecture

### Components

- **ClaudeJarvis Class**: Main application controller
- **Speech Recognition**: Converts voice to text (Google Speech API)
- **Text-to-Speech**: Converts text to voice (pyttsx3)
- **Claude API Integration**: Sends requests to Claude with tool definitions
- **Tool Executor**: Executes tools that Claude requests
- **Conversation Memory**: Maintains context across the conversation

### Available Tools

| Tool | Description |
|------|-------------|
| `execute_system_command` | Run shell commands |
| `open_website` | Open URLs in browser |
| `read_file` | Read file contents |
| `write_file` | Create/overwrite files |
| `list_directory` | List directory contents |
| `get_current_time` | Get current date/time |
| `take_screenshot` | Capture screen |
| `search_wikipedia` | Search Wikipedia |
| `play_music` | Play music files |

### Adding Custom Tools

To add new capabilities:

1. **Define the tool** in `get_tools()`:
```python
{
    "name": "my_custom_tool",
    "description": "What this tool does",
    "input_schema": {
        "type": "object",
        "properties": {
            "param1": {
                "type": "string",
                "description": "Parameter description"
            }
        },
        "required": ["param1"]
    }
}
```

2. **Implement the tool** in `execute_tool()`:
```python
elif tool_name == "my_custom_tool":
    return self._my_custom_tool(tool_input["param1"])
```

3. **Add the implementation**:
```python
def _my_custom_tool(self, param1: str) -> str:
    # Your implementation
    return "Result"
```

## Security Considerations

⚠️ **Important Security Notes:**

- Claude can execute **any system command** you allow
- Be cautious about what commands you ask Jarvis to run
- Review the tool implementations to understand what's possible
- Consider restricting `execute_system_command` for production use
- Never share your API key

### Recommended Safety Measures

1. Run in a virtual environment
2. Use a dedicated API key with usage limits
3. Monitor the conversation history
4. Add command whitelisting for sensitive operations

## Troubleshooting

### Microphone Issues
```bash
# Test microphone
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

### API Key Errors
- Verify `ANTHROPIC_API_KEY` is set correctly
- Check API key is valid in [Anthropic Console](https://console.anthropic.com/)

### Speech Recognition Errors
- Ensure you have internet connection (Google Speech API requires it)
- Check microphone permissions
- Reduce background noise

### Text-to-Speech Issues
- Linux: Install espeak (`sudo apt-get install espeak`)
- Verify pyttsx3 initialization in console output

## Customization

### Change Voice Speed
```python
self.engine.setProperty('rate', 150)  # Adjust value (default: 150)
```

### Change Voice
```python
voices = self.engine.getProperty('voices')
self.engine.setProperty('voice', voices[0].id)  # Try different indices
```

### Change Claude Model
```python
model="claude-sonnet-4-5-20250929"  # or "claude-opus-4-5-20251101"
```

### Modify System Prompt
Edit the `self.system_prompt` in `__init__()` to change Jarvis's personality or instructions.

## Cost Considerations

- Claude API usage is billed by Anthropic
- Voice commands typically use 1-5K tokens per interaction
- Long conversations with tool use may consume more tokens
- Monitor usage in [Anthropic Console](https://console.anthropic.com/)

## Comparison with Original Jarvis

| Feature | Original Jarvis | Claude-Powered Jarvis |
|---------|----------------|----------------------|
| AI Backend | OpenAI GPT | Anthropic Claude |
| Tool Calling | Limited | Native & Extensive |
| Context Memory | Limited | Full conversation |
| Task Execution | Hardcoded | AI-driven with tools |
| Extensibility | Manual functions | Add tools dynamically |
| Intelligence | GPT-4o mini | Claude Sonnet 4.5 |

## License

MIT License - See main repository for details

## Contributing

Contributions welcome! This is an educational project demonstrating Claude's tool-calling capabilities.

## Acknowledgments

- Built on the original Jarvis Desktop Voice Assistant concept
- Powered by Anthropic's Claude AI
- Uses pyttsx3 for text-to-speech
- Uses SpeechRecognition for voice input

---

**Ready to start?** Run `python claude_jarvis.py` and say hello to your AI assistant!
