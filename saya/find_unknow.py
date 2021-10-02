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
                            inline_dispatchers=[Literature("隐藏指令")]
                            ))
async def find_else(app: GraiaMiraiApplication, member: Member, group: Group):
    await app.sendGroupMessage(group, MessageChain.create([
        # At(member.id),
        Plain("目前隐藏指令有：肥啾，预订")
    ]))
