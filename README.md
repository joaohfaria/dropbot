# DropBot

A Discord bot for a fictional skin shop, built with Python as a study project.

Currently in development.

## Features

- Lists available weapon models
- Selects a model by number, with input validation

## Requirements

- Python 3
- A Discord bot token

## How to run

```bash
git clone https://github.com/joaohfaria/dropbot.git
cd dropbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root with your bot token:

DISCORD_TOKEN=your_token_here


Then run:

```bash
python bot.py
```

## Next steps

- Add prices to the catalog
- User wallet with fictional currency
- Purchase and inventory
- Data persistence