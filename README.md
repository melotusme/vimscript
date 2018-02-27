# 一个帮助写 protobuf 的vim 插件
一图胜千言

![alt](https://github.com/melotusme/vimscript/blob/master/protobuf.gif)



### usage
选中目标，然后 leader_key + c (可自行在script.py 中修改@snake.visual_key_map 参数)

本插件依赖于 [snake](https://github.com/amoffat/snake)
#### *Vundle 用户
在.vimrc 添加

Plugin 'amoffat/snake'

然后在vim中运行

:source %

:PluginInstall
#### VimPlug 用户
在.vimrc 添加

Plug 'amoffat/snake'

然后在vim中运行

:source %

:PlugInstall





在bash及与之兼容终端中
```bash
git clone https://github.com/melotusme/vimscript
cd vimscript/
ln -sv `pwd`/script.py ~/.vimrc.py
```

fish 中
```
git clone https://github.com/melotusme/vimscript
cd vimscript/
ln -sv (pwd)/script.py ~/.vimrc.py
```
