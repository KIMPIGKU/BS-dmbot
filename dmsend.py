
# 봉순#6959 : MASS DM BOT SOURCE


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.id ==569477245605904384:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="ʙᴜʀʙᴇʀʀʏ ꜱᴇʀᴠᴇʀ 공지사항", value=msg, inline=True)
                        embed.set_footer(text="MADE_BY_PINGKU")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzU4MzUzNDY3MjY5MDU0NTg1.X2tttA.vbQAcAapQniWn7iiZJc7tAfDm8Q')
