import aiohttp
from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, Plain, At

saya = Saya.current()
channel = Channel.current()
# global flag
# flag = 11


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("鸡汤")]))
async def soup(app: GraiaMiraiApplication, group: Group, member: Member):
    async with aiohttp.request(
            "GET", "http://api.btstu.cn/yan/api.php"
    ) as response:
        json_str = await response.text()
    await app.sendGroupMessage(group, MessageChain.create([
        # At(member.id),
        Plain(json_str)]))
    pass
