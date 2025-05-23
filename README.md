# Discord "Zon't" Counter Bot

A fun Discord bot inspired by the Nicki Minaj "zon't zo it" meme that tracks and counts occurrences of "zon't" and "zo" sequences in chat messages.

## What This Bot Does

This Discord bot monitors messages in your server and automatically counts whenever someone types any sequence containing "zon't" or "zo" - inspired by the viral Nicki Minaj "zon't zo it" meme. When detected, it responds with the current count.

### Pattern Detection

The bot uses regex pattern matching to detect any sequence containing "zon't" or "zo" including:
- `zon't zo it` (the original meme)
- `zon't`
- `zont`
- `zo it`
- `zo`
- And other variations with different spacing and punctuation

Basically, any message containing "zon't" or "zo" will increment the counter.

## Features

- **Real-time monitoring**: Watches all messages in channels where the bot has access
- **Pattern matching**: Detects any occurrence of "zon't" or "zo" sequences
- **Global counter**: Maintains a running count across all detected instances
- **Instant feedback**: Responds immediately when a pattern is detected

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- A Discord application/bot token
- Required Python packages (see requirements.txt)

### Installation Steps

1. **Clone this repository**
   ```bash
   git clone https://github.com/Abdalla-Eldoumani/
   cd discord-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create a `.env` file in the project root and add your Discord bot token:
   ```
   TOKEN=your_discord_bot_token_here
   ```

4. **Bot Permissions**
   Use the provided authorization URL in `bot_url.txt` to invite the bot to your server with the necessary permissions.

### Running the Bot

```bash
python discord_bot.py
```

The bot will start and print a confirmation message when successfully logged in.

## File Structure

```
├── discord_bot.py        # Main bot script
├── requirements.txt      # Python dependencies
├── discloud.config      # Deployment configuration for DisCloud hosting
├── bot_url.txt          # Discord bot invitation URL
├── .env                 # Environment variables (create this file)
└── README.md           # This file
```

## Dependencies

- `discord.py` - Discord API wrapper for Python
- `python-dotenv` - Load environment variables from .env file

## Deployment

This project includes a `discloud.config` file for easy deployment to DisCloud hosting platform:

- **Name**: mybot
- **RAM**: 100MB
- **Auto-restart**: Disabled
- **Main file**: discord_bot.py

## Bot Permissions

The bot requires the following permissions:
- Read Messages
- Send Messages
- Read Message History

## Usage

Once the bot is running and added to your server:

1. Type any message containing "zon't" or "zo" in a channel where the bot can see messages
2. The bot will automatically respond with the current count
3. The counter persists until the bot is restarted
4. Perfect for tracking how often the "zon't zo it" meme appears in your server!

## Example

```
User: zon't zo it, that's too much work
Bot: Zon't Counter: 1

User: just zo with the flow
Bot: Zon't Counter: 2

User: I zon't think this is right
Bot: Zon't Counter: 3
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).