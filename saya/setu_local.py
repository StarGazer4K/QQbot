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
                            inline_dispatchers=[Literature("涩图")]))
async def setu_local(app: GraiaMiraiApplication, member: Member, group: Group):
    if group.id == 722040415:
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Plain("抱歉，本群不支持涩图功能呢~")
        ]))
    else:
        number1 = random.randint(1, 791)
        lujing = "D:/Qqun/StarGazer4K/Image/setu/" + str(number1) + ".png"
        print(number1)
        await app.sendGroupMessage(group, MessageChain.create([
            # At(member.id),
            Image.fromLocalFile(lujing)
        ]))
