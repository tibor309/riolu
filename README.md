# Riolu
Riolu is an another discord made for my friends. It has some fun commands, but i don't really know what should be the main features of this bot. I only made this to separate some commands from my other bots.

<div id="badges", align="center">
  <a href="https://repl.it/github/tibor309/riolu">
    <img src="https://img.shields.io/badge/Replit-F26207.svg?style=for-the-badge&logo=Replit&logoColor=white&label=Run on" alt="Replit Badge"/>
  </a>
  <a href="https://glitch.com/edit/#!/import/github/tibor309/riolu">
    <img src="https://img.shields.io/badge/Glitch-3333FF.svg?style=for-the-badge&logo=Glitch&logoColor=white&label=Remix on" alt="Glitch Badge"/>
  </a>
</div>

## Setup
### Replit & Glitch
Clone the repo, then head over to the secrets tab and a new secret called `TOKEN`, and fill out the value field with your bot token. After everything set up, just click on the run button. Optionally you can enable the Flask server to make the bot run 24/7.

### Source
Install all the required packages with this command. **Make sure to install [py-cord][py-cord] instead of discord.py!**
```
pip3 install -r requirements.txt
```
After that, rename the `.env.example` file to `.env`, and fill it out with your values. If you're ready, run the bot with the `python3 main.py` command!

## Config
You can change the embed color, and the time structure for the logs in the config file.

[py-cord]: https://github.com/Pycord-Development/pycord/