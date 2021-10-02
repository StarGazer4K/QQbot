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
                            inline_dispatchers=[Literature("服务器")]
                            ))
async def mczoo(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://mcapi.us/server/status?ip=servermc.ltd&port=25565"
    ) as response:
        json_str = await response.text()
    # print(json_str)
    size_zfc = len(json_str)
    tou = json_str.index("players")
    json_str = json_str[(tou-1):]
    json_str = "{" + json_str
    # print(json_str)
    doc = json.loads(json_str)
    max_num = doc["players"]["max"]
    online = doc["players"]["now"]
    player_list = {}
    final_list = ""
    if max_num == 2019:
        if online == 0:
            await app.sendGroupMessage(group, MessageChain.create([
                Plain("空荡荡的")
            ]))
        else:
            for i in range(0, online):
                player_list[i] = doc['players']['sample'][i]['name']
                final_list += str(player_list[i])
                if i != online:
                    final_list += "\n"
                # print("player", i + 1, ":", player_list[i])
                pass
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
            Plain("获取失败")
        ]))
