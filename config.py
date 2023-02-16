import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.getenv("TOKEN") # Set token in the .env file  - NEVER SHARE YOUR TOKEN WITH ANYONE!
bot_color = 0x3ba89d # Embed color in hex (#3ba89d -> 0x3ba89d)
bot_time = "%Y-%m-%d %H:%M:%S %p UTC" # Time structure for logs