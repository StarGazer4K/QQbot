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
                            inline_dispatchers=[Literature("新闻")]
                            ))
async def news(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://api.2xb.cn/zaob"
    ) as response:
        json_str = await response.text()
    doc = json.loads(json_str)
    Image.url = doc['imageUrl']
    datatime = doc['datatime']
    await app.sendGroupMessage(group, MessageChain.create([
        Plain(datatime),
        Image.fromNetworkAddress(Image.url, )
    ]))
    pass
