import random

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
                            inline_dispatchers=[Literature("抽卡祝福")]
                            ))
async def card(app: GraiaMiraiApplication, member: Member, group: Group):
    number1 = random.randint(1, 5)
    lujing = "D:/Qqun/StarGazer4K/Image/抽卡祝福/" + str(number1)
    lujing += ".png"
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Image.fromLocalFile(lujing)
    ]))
    pass
