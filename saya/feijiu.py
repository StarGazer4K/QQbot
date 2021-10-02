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


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("肥啾")]
                            ))
async def feijiu(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://api.bilibili.com/x/relation/stat?vmid=698018684"
    ) as response:
        json_str = await response.text()
        doc = json.loads(json_str)
    following = doc['data']['following']
    follower = doc['data']['follower']
    res = "肥啾关注了" + str(following) + "人，有" + str(follower) + "个粉丝w~"
    await app.sendGroupMessage(group, MessageChain.create([
        # At(member.id),
        Plain(res)
        ]))
    pass