import asyncio
import os
import time

from graia.application import GraiaMiraiApplication, Session, MessageChain, Group
from graia.application.message.elements.internal import Plain
from graia.broadcast import Broadcast
from graia.broadcast.interrupt import InterruptControl
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.scheduler import GraiaScheduler
from graia.scheduler.saya import GraiaSchedulerBehaviour

ignore = ["__init__.py", "__pycache__"]

loop = asyncio.get_event_loop()
bcc = Broadcast(loop=loop)
scheduler = GraiaScheduler(loop, bcc)
inc = InterruptControl(bcc)

saya = Saya(bcc)
saya.install_behaviours(BroadcastBehaviour(bcc))
saya.install_behaviours(GraiaSchedulerBehaviour(scheduler))

app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:3030",
        authKey="KEYINITBftUkg3c",  # 填入 authKey
        account=2929281033,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

with saya.module_context():
    for module in os.listdir("saya"):
        if module in ignore:
            continue
        if os.path.isdir(module):
            saya.require(f"saya.{module}")
        else:
            saya.require(f"saya.{module.split('.')[0]}")


@bcc.receiver("GroupMessage")
async def friend_message_listener(message: MessageChain, group: Group, app: GraiaMiraiApplication):
    msg = message.asDisplay()
    if msg.startswith("测试"):
        await app.sendGroupMessage(group, MessageChain(__root__=[Plain("测试成功")]))


@bcc.receiver("GroupMessage")
async def friend_message_listener_1(message: MessageChain, group: Group, app: GraiaMiraiApplication):
    msg = message.asDisplay()
    if msg.startswith("123"):
        await app.sendGroupMessage(group, MessageChain(__root__=[Plain("\n")]))

app.launch_blocking()
