import aiohttp
from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, At, Image

saya = Saya.current()
channel = Channel.current()
global flag


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("动漫壁纸")]
                            ))
async def bizhi_dongman(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://api.btstu.cn/sjbz/api.php?lx=dongman&format=images"
    ) as response:
        res = str(response)
        # print(res)
        tou = res.find("http")
        wei = res.find("[200 OK]")
        # print(tou)
        # print(wei)
        res = res[tou:wei - 2]
        # print(res)
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Image.fromNetworkAddress(res, )
        ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("风景壁纸")]
                            ))
async def bizhi_fengjing(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://api.btstu.cn/sjbz/api.php?lx=fengjing&format=images"
    ) as response:
        res = str(response)
        # print(res)
        tou = res.find("http")
        wei = res.find("[200 OK]")
        # print(tou)
        # print(wei)
        res = res[tou:wei - 2]
        # print(res)
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Image.fromNetworkAddress(res, )
        ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("妹子壁纸")]
                            ))
async def bizhi_meizi(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "http://api.btstu.cn/sjbz/api.php?lx=meizi&format=images"
    ) as response:
        res = str(response)
        # print(res)
        tou = res.find("http")
        wei = res.find("[200 OK]")
        # print(tou)
        # print(wei)
        res = res[tou:wei-2]
        # print(res)
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Image.fromNetworkAddress(res, )
        ]))
    pass