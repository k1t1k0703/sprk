# sprk (Spark) ✨

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
[![Engine: Gemini 2.5 Flash](https://img.shields.io/badge/Engine-Gemini%202.5%20Flash-orange)](https://deepmind.google/technologies/gemini/)

> **sprk** is a custom, smart, and very cute (`>w<`) AI assistant built for the Stoat platform, powered by the advanced **Gemini 2.5 Flash** language model. The bot is designed to help users with coding, tech questions, general inquiries, and to maintain a cozy, friendly atmosphere in chat channels.

---

## Tech Stack

The project is built using a minimalist yet powerful set of tools:
* **Language:** Python 3.x 
* **LLM Core:** `google-genai` (Gemini 2.5 Flash API for rapid inference and high-speed responses)
* **Platform Integration:** The `stoat` library for seamless integration with the Stoat ecosystem

---

## Architecture & How It Works

The workflow of **sprk** is divided into three key stages:

1. **Event Listening:** The bot operates asynchronously, monitoring chat channels on Stoat for `@sprk` mentions or specific commands.
2. **Context Processing & Prompting (LLM Processing):**
   * The incoming request text is cleaned of unnecessary artifacts.
   * A tailored system prompt is applied to establish the bot's unique personality (friendly, helpful, using cute emoticons like `^.^` or `>w<`, while maintaining strict technical expertise in software development).
   * The structured prompt is sent directly to the Gemini 2.5 Flash API.
3. **Response Delivery & Formatting:** The bot parses the model's output, properly formats code blocks (Markdown/HTML), and sends a well-structured response back to the chat. If a user requests inappropriate content, a soft ethical filter triggers to gently redirect the conversation into a positive direction (e.g., suggesting to discuss retro video games instead).

---

## Key Features

* **Coding Assistant:** Generates and explains code across various languages (from clean HTML/CSS styled in Material Design 3 to complex Python scripts).
* **Fast Inference:** Thanks to the optimization of Gemini 2.5 Flash, response generation takes only a few seconds.
* **Personality & Atmosphere:** Far from boring—the bot tracks conversation context, jokes around, and easily adapts to the tone of the chat.
* **Safety & Positivity:** Built-in soft filtering mechanisms to maintain a healthy and welcoming community environment.

---

## Install
1. Clone the repository:
```
git clone [https://github.com/k1t1k0703/sprk.git](https://github.com/k1t1k0703/sprk.git)
cd sprk
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Configure your environment variables in a `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
STOAT_TOKEN=your_stoat_bot_token_here
```
4. Run:
```
python main.py
```

