# 配置OpenAI-gym 环境
## 1. 安装gym库
在Anaconda Prompt的对应环境中，执行命令:

`pip install gym -i  https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000`

> `-i https://pypi.tuna.tsinghua.edu.cn/simple` 表示使用清华镜像

> `--default-timeout=1000` 表示设置超时限制

安装完成后执行Test_1.py文件测试

## 2. 安装atari-py
对于win10系统，需要重新设定atari_py文件，执行命令:

`pip install --no-index -f https://github.com/Kojoley/atari-py/releases atari_py`

> 如果之前已经安装了低版本的，使用`pip uninstall atari-py` 卸载

安装完成后执行Test_2.py文件测试
