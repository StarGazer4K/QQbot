import aiohttp
from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, At, Image

import json
import random

saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("猫猫图")]
                            ))
async def bizhi_cat(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "https://api.thecatapi.com/v1/images/search"
    ) as response:
        json_str = await response.text()
        doc = json.loads(json_str)
        Image.url = doc[0]['url']
        await app.sendGroupMessage(group, MessageChain.create([
            Image.fromNetworkAddress(Image.url, )
        ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("狗狗图")]
                            ))
async def bizhi_dog(app: GraiaMiraiApplication, member: Member, group: Group):
    async with aiohttp.request(
            "GET", "https://dog.ceo/api/breeds/image/random"
    ) as response:
        json_str = await response.text()
        doc = json.loads(json_str)
        Image.url = doc['message']
        await app.sendGroupMessage(group, MessageChain.create([
            Image.fromNetworkAddress(Image.url, )
        ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("狐狸图")]
                            ))
async def bizhi_fox(app: GraiaMiraiApplication, member: Member, group: Group):
    random_num = random.randint(1, 123)
    str_fox = "https://randomfox.ca/images/" + str(random_num) + ".jpg"
    await app.sendGroupMessage(group, MessageChain.create([
        Image.fromNetworkAddress(str_fox, )
    ]))
    pass