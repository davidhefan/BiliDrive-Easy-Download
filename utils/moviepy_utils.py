from moviepy import *
from moviepy.editor import *


# pip install moviepy

def merge(video_path, audio_path, target_path):
    # 提取音轨
    audio = AudioFileClip(audio_path)
    # 读入视频
    video = VideoFileClip(video_path)
    # 将音轨合并到视频中
    video = video.set_audio(audio)
    # 输出
    video.write_videofile(target_path)
