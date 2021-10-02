import asyncio

import aiohttp
import json
from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, At, Image, Plain

saya = Saya.current()
channel = Channel.current()
global flag


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("预订")]
                            ))
async def pixiv_setu(app: GraiaMiraiApplication, member: Member, group: Group):
    if (member.id == 1278145932) or (member.id == 907489501):
        async with aiohttp.request(
                "GET", "https://api.lolicon.app/setu/v2"
        ) as response:
            json_str = await response.text()
        doc = json.loads(json_str)
        Image.url = doc['data'][0]['urls']['original']
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Image.fromNetworkAddress(Image.url, )
        ]))
        # await asyncio.sleep(60)  # 等待
        # await GraiaMiraiApplication.revokeMessage(messageId)  # 撤回
        # print(MessageChain.asDisplay())
        pass
    else:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain("LSP爬")
        ]))
        pass
    pass
