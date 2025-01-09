### HoshinoBroadcast

基于 [HoshinoBotV2](https://github.com/Ice-Cirno/HoshinoBot) 的群发消息插件

**此项目起因是某个群发插件过于垃圾导致连同一些无关的群聊也一起发送消息而诞生**

**请远离垃圾插件，避免一些不必要的尴尬时刻（**

### 环境需求
```
python 3.9+
```

### 使用说明
```
在 hoshino/config/__bot__.py 中添加本项目文件名
在群里或私信向 bot 发送 [开启 HoshinoBroadcast] 启用插件

开启 HoshinoBC                            ：启用插件
/广播 消息 -g group1 group2 group3...       ：向指定群发送消息

重启成功之后会在群聊中发送 [bot名 启动成功]
```

### 额外说明
```
可在 main.py 中添加快捷发送的群号组
详细请使用 ctrl+f 搜索：# 群组 mark
```