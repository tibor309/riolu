import aiohttp, io
import discord
from discord.ext import commands
import requests
from config import bot_color


class fun_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        
    # I win! I ALWAYS WIN!
    @discord.slash_command(name="whowouldwin", description="Place your bets now")
    @discord.option("member1", discord.Member, description="Choose a member", required=True)
    @discord.option("member2", discord.Member, description="And choose an opponent", required=True)
    async def win(self, ctx, member1: discord.Member, member2: discord.Member):
        api = "https://api.popcat.xyz/whowouldwin"
        first = member1.avatar
        second = member2.avatar
        url = f"{api}?user1={first}&user2={second}"
        
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.respond(file=discord.File(imageData, f'image0.png'), ephemeral=False)  


    # Ship members ~Together forever
    @discord.slash_command(name="ship", description="I think they like eachother")
    @discord.option("member1", discord.Member, description="Choose a member", required=True)
    @discord.option("member2", discord.Member, description="And their partner", required=True)
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        api = "https://api.popcat.xyz/ship"
        first = member1.avatar
        second = member2.avatar
        url = f"{api}?user1={first}&user2={second}"
        
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(url) as trigImg:
                imageData = io.BytesIO(await trigImg.read())
                await trigSession.close()
                await ctx.respond(file=discord.File(imageData, f'image1.png'), ephemeral=False)  
                


    # Create a fake yt comment
    @discord.slash_command(name="ytcomment", description="Create a fake yt comment")
    @discord.option("title", str, description="An interesting title", required=True)
    @discord.option("avatar", discord.Attachment, description="profile pic", required=True)
    @discord.option("username", str, description="username", required=True)
    @discord.option("comment", str, description="This comment is sponsored by NordVPN", required=True)
    async def yt(self, ctx, title: str, avatar: discord.Attachment, username: str, comment: str):
        api = "https://some-random-api.ml/canvas/youtube-comment"
        avatar_url = avatar.url

        await ctx.defer()
        if not avatar_url.lower().endswith(('.png', '.jpg', '.jpeg')):
            return await ctx.respond("Invalid attachment type! Use only png or jpg/jpeg files!", ephemeral=True)
            
        name = username.replace(" ", "+")
        text = comment.replace(" ", "+")
        url=f"{api}?avatar={avatar_url}&username={name}&comment={text}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "thefunny.png")
                    
                    embed = discord.Embed(color=bot_color, title=title)
                    embed.set_image(url="attachment://thefunny.png")
                    await ctx.followup.send(embed=embed, file=file)
                else:
                    await ctx.followup.send('Failed to get the image :(', ephemeral=True)
                await session.close()



    # Funny 8ball
    @discord.slash_command(name="8ball", description="Talk to the magic ball")
    @discord.option("question", str, description="What is your question?", required=True)
    async def ball(self, ctx, question:str):
        api = "https://api.popcat.xyz/8ball"

        await ctx.defer()
        response = requests.get(api, verify=True)
        data = response.json()
        embed = discord.Embed(color=bot_color, description=f"🎱 " + data['answer'])
        await ctx.followup.send(f"> {question}", embed=embed)
        

    # Love is in the air? Wrong, gas leak
    @discord.slash_command(name="pickuplines", description="Yo shawty, take me out to dinner")
    async def pickuplines(self, ctx):
        api = "https://api.popcat.xyz/pickuplines"

        await ctx.defer()
        response = requests.get(api, verify=True)
        data = response.json()
        embed = discord.Embed(color=bot_color, description=data['pickupline'])
        await ctx.followup.send(embed=embed)

        

def setup(bot):
    bot.add_cog(fun_commands(bot))