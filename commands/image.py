import aiohttp, io
import discord
from discord.ext import commands

api1 = "https://api.popcat.xyz" # Apis for images
api2 = "https://some-random-api.ml"
api3 = "https://api.jeyy.xyz"

class image_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Create group for commands
    imgedit = discord.SlashCommandGroup("imgedit", "Lets you edit images (images can take a while to load)")

    # Add filter to images
    @imgedit.command(name="filter", description="Add filters to images")
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("filter", str, description="Select a filter", choices=["glass", "gay", "pixelate", "blur", "invert", "grayscale", "lines", "glitch", "stereo", "cartoon", "matrix"], required=True)
    async def filter(self, ctx, member: discord.Member, filter: str):
        avatar = member.avatar

        if filter == "glass":
            url = f"{api2}/canvas/glass?avatar={avatar}"
            ext = "png"
        elif filter == "gay":
            url = f"{api2}/canvas/gay?avatar={avatar}"
            ext = "png"
        elif filter == "pixelate":
            url = f"{api2}/canvas/pixelate?avatar={avatar}"
            ext = "png"
        elif filter == "blur":
            url = f"{api1}/blur?image={avatar}"
            ext = "png"
        elif filter == "invert":
            url = f"{api1}/invert?image={avatar}"
            ext = "png"
        elif filter == "grayscale":
            url = f"{api1}/greyscale?image={avatar}"
            ext = "png"

        elif filter == "lines":
            url = f"{api3}/image/lines?image_url={avatar}"
            ext = "png"
        elif filter == "glitch":
            url = f"{api3}/image/glitch?image_url={avatar}&level=3"
            ext = "gif"
        elif filter == "stereo":
            url = f"{api3}/image/stereo?image_url={avatar}"
            ext = "png"
        elif filter == "cartoon":
            url = f"{api3}/image/cartoon?image_url={avatar}"
            ext = "png"
        elif filter == "matrix":
            url = f"{api3}/image/matrix?image_url={avatar}"
            ext = "gif"

        await ctx.defer()
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg: # get users avatar with the image
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                await trigSession.close() # closing the session
                await ctx.followup.send(file=discord.File(imageData, f'image.{ext}'), ephemeral=True) # sending the file

                
        
    # Add overlays to uploaded images
    @imgedit.command(name="overlay", description="Add different overlays to images")
    @discord.option("member", discord.Member, description="Select a member", required=True)
    @discord.option("overlay", str, description="Select an overlay", choices=["uncover", "ad", "pet", "clown", "gun", "wanted", "communism" "triggered", "kanye"], required=True)
    async def overlay(self, ctx, member: discord.Member, overlay: str):
        avatar = member.avatar

        if overlay == "uncover":
            url = f"{api1}/uncover?image={avatar}"
            ext = "png"
        elif overlay == "ad":
            url = f"{api1}/ad?image={avatar}"
            ext = "png"
        elif overlay == "pet":
            url = f"{api1}/pet?image={avatar}"
            ext = "gif"
        elif overlay == "clown":
            url = f"{api1}/clown?image={avatar}"
            ext = "png"
        elif overlay == "gun":
            url = f"{api1}/gun?image={avatar}"
            ext = "png"
        elif overlay == "wanted":
            url = f"{api1}/wanted?image={avatar}"
            ext = "png"
        elif overlay == "communism":
            url = f"{api1}/communism?image={avatar}"
            ext = "png"
       
        elif overlay == "triggered":
            url = f"{api2}/canvas/triggered?avatar={avatar}"
            ext = "gif"

        elif overlay == "kanye":
            url = f"{api3}/image/kanye?image_url={avatar}"
            ext = "png"
        
        await ctx.defer()
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.followup.send(file=discord.File(imageData, f'image.{ext}'), ephemeral=True)  

        

def setup(bot):
    bot.add_cog(image_commands(bot))