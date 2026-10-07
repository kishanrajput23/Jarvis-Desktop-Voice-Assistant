# Jarvis Desktop Voice Assistant🔥

<img src="https://giffiles.alphacoders.com/212/212508.gif" alt="">

**Have you ever wondered how cool it would be to have your own assistant? Imagine how easier it would be doing Wikipedia searches without opening web browsers, and performing many other daily tasks like playing music with the help of a single voice command, opening different browsers in just a voice command.**

**This project is simple desktop voice assistant built with python named as “Jarvis Desktop Voice Assistant”. This project is fully completed and error free. It was compiled in VS Code Editor.**

**🔸 Let's be honest, it's not as intelligent as in the movie, but it can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.**

## 📌Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## 📌 Features

Jarvis is now more powerful and bilingual! Some of its key features include:

- **Bilingual Support (FR/EN)**: Native ability to understand and respond in both French and English.
- **Cross-Platform**: Fully compatible with Linux (Fedora, Ubuntu/Debian) and Windows.
- **Greet User**: Greets you based on the time of day.
- **Time & Date**: Tells you the current time and date in the chosen language.
- **System Control**: Restart or Shut down your system via voice commands.
- **Web Browsing**: Open YouTube, Google, or any website.
- **Wikipedia**: Search for information and get a voice summary.
- **Entertainment**: Play music from your local library or tell jokes.
- **Productivity**: Take screenshots and save notes.

## 📌 Key Advantages

Why choose this version of Jarvis?

1.  **Seamless Bilingualism**: No need to manually switch languages. Jarvis detects the intent and adapts its voice and vocabulary dynamically.
2.  **Linux Ready**: Optimized for modern Linux environments using `systemctl` for power management and `xdg-open` for media.
3.  **Modular Architecture**: Built with a centralized translation system (`STRINGS` dictionary), making it extremely easy to add new languages or modify existing ones.
4.  **Zero-Latency Logic**: Optimized command handling replacing complex decision trees with a lean, mapping-based approach.
5.  **Clean & Maintainable**: Refactored according to NASA-inspired coding standards for maximum reliability.

## Requirements

Python 3.6+

## 📌Installation

1. **Fork The Repository**
   - Click the "Fork" button on the top right corner of the repository page.

2. **Clone The Repository**
   - Clone the forked repository to your local machine:
     ```bash
     git clone <URL>
     cd Jarvis-Desktop-Voice-Assistant
     ```

3.  **Create and Activate a Virtual Environment**
     - Create a virtual environment:
     ```bash
     python -m venv .venv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```bash
       .venv\Scripts\activate
       ```
     - For macOS/Linux:
       ```bash
       source .venv/bin/activate
       ```
   - This activates the virtual environment and should look like `(venv) directory/of/your/project>`

### 4. Install Requirements

- Install all the requirements given in **[requirements.txt](https://github.com/kishanrajput23/Jarvis-Desktop-Voice-Assistant/blob/main/requirements.txt)** by running the command `pip install -r requirements.txt`

### 5. System Prerequisites (Linux Only)

Before running Jarvis on Linux, you need to install some system dependencies:

- **For Ubuntu/Debian:**
  ```bash
  sudo apt-get install -y python3-tk python3-dev scrot
  ```
- **For Fedora:**
  ```bash
  sudo dnf install -y python3-tkinter python3-devel scrot
  ```

### 6. Install PyAudio
   - Follow the instructions given **[here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14)**

6. **Run the Assistant**
  - Run the main script:
    ```bash
    python jarvis.py
    ```
  - Now Enjoy with your own assistant !!!!

7. **Deactivate the Virtual Environment**
   - After you're done, deactivate the virtual environment:
     ```bash
     deactivate
     ```

## 📌Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📌Author

👤 **Kishan Kumar Rai**

- Twitter: [@kishan_rajput23](https://twitter.com/kishan_rajput23)
- Github: [@kishanrajput23](https://github.com/kishanrajput23)
- LinkedIn: [@kishan-kumar-rai](https://linkedin.com/in/kishan-kumar-rai-23112000)

## 📌Show your support

Please ⭐️ this repository if this project helped you!

## 📌License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 📌Learning Resources to Extend This Project

To build this project further and enhance its capabilities, a strong understanding of the following areas is recommended:

### 🐍 Python Fundamentals
Python is the core language behind this project. A solid grasp of syntax, control flow, functions, and error handling will help you modify and extend the assistant’s functionality.  
👉 [Python Programming Course](https://www.mygreatlearning.com/academy/premium/master-python-programming)

### 🎙️ Voice Processing & NLP
Voice commands are processed using speech and text-based techniques. Understanding Natural Language Processing (NLP) concepts such as tokenization and text analysis can help improve voice interaction.  
👉 [Introduction to NLP](https://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-natural-language-processing)

### 🤖 Intelligence & Generative AI
Currently, the assistant follows predefined logic. By integrating Generative AI concepts, it can be enhanced into a conversational assistant capable of generating intelligent responses and performing web-based tasks.  
👉 [Introduction to Generative AI](https://www.mygreatlearning.com/academy/premium/master-generative-ai)

### 👁️ Computer Vision
To make the assistant more advanced, computer vision can be introduced for features like face detection and gesture control. Learning image and video processing fundamentals is a good starting point.  
👉 [Computer Vision Essentials](https://www.mygreatlearning.com/academy/learn-for-free/courses/computer-vision-essentials)

### 📄 Related Reading
For a conceptual overview of building voice assistants in Python, you can refer to this article: [CLICK HERE](https://www.mygreatlearning.com/blog/jarvis-desktop-assistant-python-project/)

---

> *Some learning resources mentioned above are shared as part of an educational collaboration.*
