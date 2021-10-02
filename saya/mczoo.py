import aiohttp
import json
from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, At, Plain

saya = Saya.current()
channel = Channel.current()
global flag


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("备用服务器")]
                            ))
async def mczoo(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "https://api.miri.site/mcPlayer/get.php?ip=bm.lafamc.com&port=996"
    ) as response:
        json_str = await response.text()
    doc = json.loads(json_str)
    # print(f"doc:{doc}")
    online = doc['online']
    player_list = {}
    final_list = ""
    if online != 0:
        for i in range(0, online):
            player_list[i] = doc['sample'][i]['name']
            final_list += str(player_list[i])
            if i != online:
                final_list += "\n"
            # print("player", i + 1, ":", player_list[i])
            pass
        # final_list = final_list[:-2]
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Plain("在线人数："),
            Plain(online),
            Plain("\n"),
            Plain(final_list)
        ]))
        pass
    else:
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Plain("空荡荡的")
        ]))
