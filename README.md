# Muiz Bot

## Install Libraries:
```bash
py -m pip install discord.py
py -m pip install python-dotenv
```

## Commands

|Command|Usage|Description|
|-------|-----|-----------|
|Help|```--help```|Displays the help menu with all available commands.|
|Version|```--version```|Shows the bot's current version and release date.|
|Kick|```--kick @user [reason]```|Kicks the mentioned user from the server.|
|Ban|```--ban @user [reason]```|Bans the mentioned user from the server.|
|Unban|```--unban User#1234```|Unbans a user using their username/ID.|

## Installation & Setup

### Prerequisites:
Python 3.8 or higher installed

A Discord Bot Token from the Discord Developer Portal

### Clone & Install:

#### Clone the repository and install the necessary libraries:

```
git clone https://github.com/muizmohammed/discord-bot.git

cd discord-bot

py -m pip install -r requirements.txt
```

### .env File

To keep the bot secure, the Bot Token is not included in the source code. You must provide your own by creating a .env file.

Why? If you upload your token to GitHub, Discord will automatically disable it to protect your account.

### Run the Program
```bash
py bot.py
```
#### How to set it up:
1. Create a new file in the main folder named exactly .env.

2. Open the file and paste the following line, replacing ```YOUR_TOKEN_HERE``` with your actual token from the Discord Developer Portal:

    ```DISCORD_TOKEN=YOUR_TOKEN_HERE```

3. Make sure your ```.gitignore``` file contains ```.env``` so you don't accidentally upload your secret token!

## Made by Muiz
### Linkedin: https://www.linkedin.com/in/muiz-mohammed-28a4362a4/
### Discord: muiz_
