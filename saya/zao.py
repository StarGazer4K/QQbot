import random

from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, Plain, At

saya = Saya.current()
channel = Channel.current()
global flag


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("早")]))
async def zao(app: GraiaMiraiApplication, group: Group, member: Member):
    num = random.randint(1, 5)
    if num == 1:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain(" 早呀")]))
    elif num == 2:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain(" 早上好")]))
    elif num == 3:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain(" 你理智溢出了（小声")]))
    elif num == 4:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain(" 你昨晚真棒！")]))
    elif num == 4:
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),
            Plain(" 群主昨晚棒吗？")]))
    pass
