import os
from dotenv import load_dotenv
load_dotenv()


bot_prefix = "?"
bot_token = os.getenv("TOKEN")

bot_color = 0x3ba89d
bot_time = "%Y-%m-%d %H:%M:%S %p UTC"