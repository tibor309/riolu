# Riolu
Rialu is a discord bot that allows you to create funny images of others. Currently i don't really know what should be the main features of this bot. Suggestions are always welcome!

<div id="badges", align="center">
  <a href="https://replit.com/@Tibor309/Riolu">
    <img src="https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white" alt="Replit Badge"/>
  </a>
  <a href="https://discord.com/api/oauth2/authorize?client_id=768765742093959179&permissions=51200&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/Discord-5662f6?style=for-the-badge&logo=discord&logoColor=white" alt="Discord invite Badge"/>
  </a>
</div>

## Setup
### Replit
Click on the Replit button above, and clone my repl. Then head over to the secrets tab and a new secret called `TOKEN`, and fill out the value field with your bot token. After everything set up, just click on the run button You can change more stuff in the config if you want! Optionally you can enable the Flask server to make the bot run 24/7.

### Source
If you prefer it you can host your own copy of this bot! First, install all the required packages with this command. **Make sure you install [py-cord][py-cord] instead of discord.py!**
```
pip3 install -r requirements.txt
```
Then create an `.env` file, and put your bot token in it like below. **Never share your token with anyone!**
```
TOKEN = "your bot token"
```

If you're ready, run the bot with the `python3 main.py` command!

[py-cord]: https://github.com/Pycord-Development/pycord/