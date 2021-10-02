from graia.saya import Saya, Channel
from graia.application.group import Group, Member
from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.message.parser.literature import Literature
from graia.application.message.elements.internal import MessageChain, Plain, At

# from timer import flag

saya = Saya.current()
channel = Channel.current()
global flag


# flag = 10


@channel.use(ListenerSchema(listening_events=[GroupMessage],
                            inline_dispatchers=[Literature("查询")]
                            ))
async def find(app: GraiaMiraiApplication, group: Group):
    if group.id == 722040415:
        await app.sendGroupMessage(group, MessageChain.create([
            Plain("目前指令有：服务器，鸡汤，新闻，动漫壁纸，风景壁纸，妹子壁纸，猫猫图，狗狗图，狐狸图")
        ]))
    else:
        await app.sendGroupMessage(group, MessageChain.create([
            Plain("目前指令有：喵一个，涩图，鸡汤，新闻，动漫壁纸，风景壁纸，妹子壁纸，猫猫图，狗狗图，狐狸图，gif，抽卡祝福，早")
        ]))
    pass
