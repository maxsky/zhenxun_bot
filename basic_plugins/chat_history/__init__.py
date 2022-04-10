from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageEvent
from models.chat_history import ChatHistory
from ._rule import rule
from configs.config import Config
from nonebot import on_message


Config.add_plugin_config(
    "chat_history",
    "FLAG",
    True,
    help_="是否开启消息自从存储",
    name="消息存储",
    default_value=True
)


chat_history = on_message(rule=rule)

# test = on_command("aa")


@chat_history.handle()
async def _(event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        await ChatHistory.add_chat_msg(event.user_id, event.group_id, str(event.get_message()))
    else:
        await ChatHistory.add_chat_msg(event.user_id, None, str(event.get_message()))

# @test.handle()
# async def _(event: MessageEvent):
#     print(await ChatHistory.get_user_msg(event.user_id, "private"))
#     print(await ChatHistory.get_user_msg_count(event.user_id, "private"))
#     print(await ChatHistory.get_user_msg(event.user_id, "group"))
#     print(await ChatHistory.get_user_msg_count(event.user_id, "group"))
#     print(await ChatHistory.get_group_msg(event.group_id))
#     print(await ChatHistory.get_group_msg_count(event.group_id))
