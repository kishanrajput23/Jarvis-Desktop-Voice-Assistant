#!/usr/bin/env python3
"""
Claude-Powered Jarvis Voice Assistant
A desktop voice assistant using Anthropic's Claude API with tool calling capabilities.
"""

import os
import sys
import json
import datetime
import webbrowser
import subprocess
import platform
from pathlib import Path
from typing import List, Dict, Any, Optional

import pyttsx3
import speech_recognition as sr
from anthropic import Anthropic

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, will use system environment variables


class ClaudeJarvis:
    """Voice assistant powered by Claude with tool execution capabilities."""

    def __init__(self):
        """Initialize the voice assistant."""
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

        # Get available voices and set to a good default
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()

        # Initialize Claude client
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        self.client = Anthropic(api_key=api_key)

        # Conversation history
        self.conversation_history: List[Dict[str, Any]] = []

        # System prompt
        self.system_prompt = """You are Jarvis, a helpful desktop voice assistant. You can help users with:
- Answering questions and having conversations
- Opening websites and applications
- Managing files (reading, writing, listing directories)
- Taking screenshots
- Playing music
- Running system commands
- Searching Wikipedia
- Telling the time and date
- And much more!

You have access to various tools to complete these tasks. Use them when needed to help the user.
Keep your responses conversational and concise since they will be spoken aloud.
When you successfully complete a task using tools, confirm it briefly."""

        print("Claude-Powered Jarvis initialized successfully!")

    def speak(self, text: str):
        """Convert text to speech."""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> Optional[str]:
        """Listen for voice input and convert to text."""
        with sr.Microphone() as source:
            print("\nListening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")

                # Use Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                print(f"You: {text}")
                return text.lower()

            except sr.WaitTimeoutError:
                print("No speech detected")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio")
                self.speak("Sorry, I didn't catch that.")
                return None
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
                self.speak("Sorry, there was an error with speech recognition.")
                return None

    def get_tools(self) -> List[Dict[str, Any]]:
        """Define the tools available to Claude."""
        return [
            {
                "name": "execute_system_command",
                "description": "Execute a shell command on the system. Use this for running programs, system operations, etc. Returns the command output.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "The shell command to execute"
                        }
                    },
                    "required": ["command"]
                }
            },
            {
                "name": "open_website",
                "description": "Open a website in the default web browser.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "The URL to open (e.g., 'https://www.google.com')"
                        }
                    },
                    "required": ["url"]
                }
            },
            {
                "name": "read_file",
                "description": "Read the contents of a file.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the file to read"
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to a file (creates or overwrites).",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the file to write"
                        },
                        "content": {
                            "type": "string",
                            "description": "Content to write to the file"
                        }
                    },
                    "required": ["file_path", "content"]
                }
            },
            {
                "name": "list_directory",
                "description": "List contents of a directory.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the directory to list (default: current directory)"
                        }
                    },
                    "required": []
                }
            },
            {
                "name": "get_current_time",
                "description": "Get the current time and date.",
                "input_schema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            {
                "name": "take_screenshot",
                "description": "Take a screenshot and save it.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "filename": {
                            "type": "string",
                            "description": "Optional filename for the screenshot (default: screenshot_TIMESTAMP.png)"
                        }
                    },
                    "required": []
                }
            },
            {
                "name": "search_wikipedia",
                "description": "Search Wikipedia for information on a topic.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The topic to search for"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "play_music",
                "description": "Play a random music file from the user's Music directory.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "genre": {
                            "type": "string",
                            "description": "Optional genre or keyword to filter music files"
                        }
                    },
                    "required": []
                }
            }
        ]

    def execute_tool(self, tool_name: str, tool_input: Dict[str, Any]) -> str:
        """Execute a tool and return the result."""
        try:
            if tool_name == "execute_system_command":
                return self._execute_system_command(tool_input["command"])

            elif tool_name == "open_website":
                return self._open_website(tool_input["url"])

            elif tool_name == "read_file":
                return self._read_file(tool_input["file_path"])

            elif tool_name == "write_file":
                return self._write_file(tool_input["file_path"], tool_input["content"])

            elif tool_name == "list_directory":
                path = tool_input.get("path", ".")
                return self._list_directory(path)

            elif tool_name == "get_current_time":
                return self._get_current_time()

            elif tool_name == "take_screenshot":
                filename = tool_input.get("filename")
                return self._take_screenshot(filename)

            elif tool_name == "search_wikipedia":
                return self._search_wikipedia(tool_input["query"])

            elif tool_name == "play_music":
                genre = tool_input.get("genre")
                return self._play_music(genre)

            else:
                return f"Error: Unknown tool '{tool_name}'"

        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

    def _execute_system_command(self, command: str) -> str:
        """Execute a system command."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            output = result.stdout.strip()
            if result.stderr:
                output += f"\nErrors: {result.stderr.strip()}"
            return output or "Command executed successfully"
        except subprocess.TimeoutExpired:
            return "Command timed out after 30 seconds"
        except Exception as e:
            return f"Error: {str(e)}"

    def _open_website(self, url: str) -> str:
        """Open a website in the default browser."""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        webbrowser.open(url)
        return f"Opened {url} in browser"

    def _read_file(self, file_path: str) -> str:
        """Read a file's contents."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return content if content else "File is empty"
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def _write_file(self, file_path: str, content: str) -> str:
        """Write content to a file."""
        try:
            # Create directory if it doesn't exist
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

    def _list_directory(self, path: str) -> str:
        """List directory contents."""
        try:
            items = os.listdir(path)
            if not items:
                return "Directory is empty"
            return "\n".join(sorted(items))
        except Exception as e:
            return f"Error listing directory: {str(e)}"

    def _get_current_time(self) -> str:
        """Get current time and date."""
        now = datetime.datetime.now()
        return now.strftime("Current time: %I:%M %p\nCurrent date: %A, %B %d, %Y")

    def _take_screenshot(self, filename: Optional[str] = None) -> str:
        """Take a screenshot."""
        try:
            import pyautogui

            if not filename:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"

            # Save to Pictures directory
            pictures_dir = Path.home() / "Pictures"
            pictures_dir.mkdir(exist_ok=True)
            filepath = pictures_dir / filename

            pyautogui.screenshot(str(filepath))
            return f"Screenshot saved to {filepath}"
        except Exception as e:
            return f"Error taking screenshot: {str(e)}"

    def _search_wikipedia(self, query: str) -> str:
        """Search Wikipedia."""
        try:
            import wikipedia
            summary = wikipedia.summary(query, sentences=3)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple results found. Please be more specific. Options: {', '.join(e.options[:5])}"
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{query}'"
        except Exception as e:
            return f"Error searching Wikipedia: {str(e)}"

    def _play_music(self, genre: Optional[str] = None) -> str:
        """Play music from the Music directory."""
        try:
            import random

            music_dir = Path.home() / "Music"
            if not music_dir.exists():
                return "Music directory not found"

            # Find music files
            music_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']
            music_files = []

            for ext in music_extensions:
                music_files.extend(music_dir.glob(f"**/*{ext}"))

            if not music_files:
                return "No music files found in Music directory"

            # Filter by genre if specified
            if genre:
                filtered = [f for f in music_files if genre.lower() in f.name.lower()]
                music_files = filtered if filtered else music_files

            # Pick a random song
            song = random.choice(music_files)

            # Open with default player
            if platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', str(song)])
            elif platform.system() == 'Windows':
                os.startfile(str(song))
            else:  # Linux
                subprocess.run(['xdg-open', str(song)])

            return f"Now playing: {song.name}"
        except Exception as e:
            return f"Error playing music: {str(e)}"

    def process_with_claude(self, user_input: str) -> str:
        """Process user input with Claude and execute any requested tools."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Call Claude API with tool support
        response = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            system=self.system_prompt,
            messages=self.conversation_history,
            tools=self.get_tools()
        )

        # Process the response and handle tool calls
        final_response = ""

        while response.stop_reason == "tool_use":
            # Build assistant message with tool uses
            assistant_message = {"role": "assistant", "content": response.content}
            self.conversation_history.append(assistant_message)

            # Execute tools and collect results
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"Executing tool: {block.name}")
                    result = self.execute_tool(block.name, block.input)
                    print(f"Result: {result[:100]}...")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            # Send tool results back to Claude
            self.conversation_history.append({
                "role": "user",
                "content": tool_results
            })

            # Get next response
            response = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=4096,
                system=self.system_prompt,
                messages=self.conversation_history,
                tools=self.get_tools()
            )

        # Extract final text response
        for block in response.content:
            if hasattr(block, 'text'):
                final_response += block.text

        # Add final response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response.content
        })

        return final_response.strip()

    def greet(self):
        """Greet the user based on time of day."""
        hour = datetime.datetime.now().hour

        if hour < 12:
            greeting = "Good morning!"
        elif hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"

        self.speak(f"{greeting} I'm Jarvis, powered by Claude. How can I help you today?")

    def run(self):
        """Main loop for the voice assistant."""
        self.greet()

        while True:
            # Listen for user input
            user_input = self.listen()

            if not user_input:
                continue

            # Check for exit commands
            if any(word in user_input for word in ['exit', 'quit', 'goodbye', 'bye']):
                self.speak("Goodbye! Have a great day!")
                break

            # Process with Claude
            try:
                response = self.process_with_claude(user_input)
                self.speak(response)
            except Exception as e:
                print(f"Error: {e}")
                self.speak("Sorry, I encountered an error processing your request.")


def main():
    """Main entry point."""
    try:
        jarvis = ClaudeJarvis()
        jarvis.run()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
