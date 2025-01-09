from . import *
from hoshino.typing import CQEvent
from hoshino import priv


@sv.on_prefix("/广播", "/s 广播")
async def broadcast(bot, ev: CQEvent):
    if not priv.check_priv(ev, priv.SUPERUSER):
        return

    args = str(ev.message).split()
    
    if "--group" not in args and "-g" not in args:
        await bot.finish(ev, "参数错误！请使用 '--group' 或 '-g' 指定群聊。\n 例如：/广播 HelloWorld --group 123456789 ")
        return

    group_index = args.index("--group") if "--group" in args else args.index("-g")
    msg = " ".join(args[:group_index]).encode("utf-8").decode("unicode_escape")
    groups = args[group_index + 1:]
    
    try:
        if len(groups) == 1:
            group_name = groups[0]
            # 群组 mark
            '''群组示例：
            if group_name == "测试":
                groups = ['123456789', '987654321', '543216789']
            '''
            if group_name == "测试":
                groups = ['ev.group_id']
            
            else:
                await bot.finish(ev, f"未知的组名：{group_name}")
    except Exception as e:
        await bot.finish(ev, f"未知的群号：{e}")
    
    if not groups:
        await bot.finish(ev, "未指定群组 ID！")
        return

    for group_id in groups:
        try:
            # 确保 group_id 是 int 类型
            group_id = int(group_id)
            await bot.send_group_msg(group_id=group_id, message=msg)
        except ValueError:
            await bot.send_private_msg(user_id=ev.user_id, message=f"无效的群组 ID：{group_id}")
        except Exception as e:
            await bot.send_private_msg(user_id=ev.user_id, message=f"向群 {group_id} 发送消息失败: {str(e)}")
