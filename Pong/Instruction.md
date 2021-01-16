# 常见错误
## 1. 提示未安装cv2，其实是安装opencv-python
安装：`pip install opencv-python -i  https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000`

## 2. 提示未安装ffmpeg，或Unknown encoder 'libx264'
安装：`conda install -c conda-forge ffmpeg`

## 3. 输出的视频只有1KB，且无法打开
该错误是github上原始文件的一个bug，需要在本地进行修改

打开文件 E:\anaconda\envs\pytorch\Lib\site-packages\gym\wrappers\monitoring\video_recorder.py 

代码`self.proc.stdin.write(frame.tobytes())` 前面去掉一个空格
