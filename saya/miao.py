import random

from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, Plain, At, Image

saya = Saya.current()
channel = Channel.current()
global flag


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("喵一个")]))
async def miao(app: GraiaMiraiApplication, member: Member, group: Group):
    number1 = random.randint(1, 4)
    print(number1)
    if number1 == 1:
        number2 = random.randint(16, 80)
        print(number2)
        lujing = "D:/Qqun/StarGazer4K/Image/表情包/" + str(number2)
        lujing += ".png"
    else:
        number2 = random.randint(1, 15)
        print(number2)
        lujing = "D:/Qqun/StarGazer4K/Image/表情包/" + str(number2)
        lujing += ".png"
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Image.fromLocalFile(lujing)
    ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("喵两个")]))
async def miao_two(app: GraiaMiraiApplication, member: Member, group: Group):
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Plain(" 得寸进尺是吧")
    ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("喵三个")]))
async def miao_three(app: GraiaMiraiApplication, member: Member, group: Group):
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Plain(" 无法无天是吧")
    ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("喵四个")]))
async def miao_four(app: GraiaMiraiApplication, member: Member, group: Group):
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Plain(" 你是不是来找茬的！")
    ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("喵五个")]))
async def miao_five(app: GraiaMiraiApplication, member: Member, group: Group):
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Plain(" 没了")
    ]))
    pass


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("群主喵一个")]))
async def miao_qunzhu(app: GraiaMiraiApplication, member: Member, group: Group):
    lujing = "D:/Qqun/StarGazer4K/Image/表情包/11.png"
    await app.sendGroupMessage(group, MessageChain.create([
        At(member.id),
        Plain(" 群主她很不情愿地满足了你~"),
        Image.fromLocalFile(lujing)
    ]))
    pass
