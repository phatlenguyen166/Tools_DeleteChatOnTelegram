# Tools to Delete Chats on Telegram

This project provides a set of tools that help users manage and delete conversations on Telegram. It allows you to interact with your Telegram account through the Telegram Bot API and remove chats based on specific criteria, such as pinned messages, folders, and exclude certain groups/bots.

## Features

- Display all Telegram conversations.
- Delete conversations by ID.
- Remove all conversations except those in the excluded list (e.g., certain bots, pinned chats, etc.).
- Prompt for confirmation before deleting any chat.

## Prerequisites

Before running this tool, make sure you have the following:

- A **Telegram API ID** and **API Hash**. You can get these from [Telegram's official website](https://my.telegram.org/auth).
- A **Telegram bot token**. You can create a new bot by chatting with [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
- Python 3.6+ installed.
- Virtual environment to manage dependencies.

## Setup

1.**Clone the repository:**

    git clone https://github.com/phatlenguyen166/Tools_DeleteChatOnTelegram.git
    cd Tools_DeleteChatOnTelegram

2.**Create a virtual environment:**

    For Windows:

    python -m venv venv

    For macOS/Linux:

    python3 -m venv venv

3.**Activate the virtual environment**:

    For Windows:

    .\venv\Scripts\activate

    For macOS/Linux:
    
    source venv/bin/activate

4.**Install the dependencies:**:

    pip install -r requirements.txt

5.**Set up environment variables:**:

    Create a .env file in the project root directory with the following content:
    API_ID=your_telegram_api_id
    API_HASH=your_telegram_api_hash
    Replace your_telegram_api_id and your_telegram_api_hash with your actual credentials.

## Usage

1.**Run the main script:**:
   
    python main.py
