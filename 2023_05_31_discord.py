import discord
import haksik_test
from discord.ext import commands
from haksik_test import get_output

output = get_output()

shard_id = 0  # 예시 샤드 ID (원하는 값을 입력하세요)
shard_count = 1  # 예시 전체 샤드 개수 (실제 적용하는 전체 샤드 수에 맞게 설정하세요)

client = commands.Bot(command_prefix='/', intents=discord.Intents.all(),  shard_id=shard_id, shard_count=shard_count)
TOKEN_KEY = 'MTExMzEyNzA2Mjg4NzIyMzQ2Nw.GGG5on.KOOd_kXYTV_p4oYuq_Iy2shmOFInpb0c5qfbzk'

@client.command()
async def 안녕(cxt):
    await cxt.channel.send(output)

client.run(TOKEN_KEY)