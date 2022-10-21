#!/usr/bin/env python

import os
import json
import shutil
from utils import myutils, config_process, moviepy_utils, ffmpeg_utils

src_bili_path = config_process.src_bili_path
src_json_encode = config_process.src_json_encode
det_bili_path = config_process.det_bili_path

if not os.path.exists(det_bili_path):
    os.makedirs(det_bili_path)

data_list = []

file_paths = myutils.walkFile(src_bili_path, [], '.m4s')

for idx, file_path_t in enumerate(file_paths):
    # 数据文件位置
    file_path = file_path_t[0]
    file_name_all = file_path_t[1]
    file_name = file_path_t[2]

    if file_name == 'video':
        print(idx, file_path, file_name_all, file_name)

        file_path_contents = file_path.split(os.path.sep)

        src_video_path = file_path
        src_audio_path = os.path.sep.join(file_path_contents[0:-1]) + os.path.sep + 'audio.m4s'
        json_name = os.path.sep.join(file_path_contents[0:-2]) + os.path.sep + 'entry.json'
        target_video_path = os.path.sep.join(file_path_contents[0:-1]) + os.path.sep + 'video.mp4'
        target_audio_path = os.path.sep.join(file_path_contents[0:-1]) + os.path.sep + 'audio.mp3'
        target_video_audio_path = os.path.sep.join(file_path_contents[0:-1]) + os.path.sep + 'video_audio.mp4'
        print('src_audio_path: ', src_audio_path)
        print('src_video_path: ', src_video_path)
        print('json_name: ', json_name)

        if not os.path.exists(target_audio_path):
            shutil.copyfile(src_audio_path, target_audio_path)
        if not os.path.exists(target_video_path):
            shutil.copyfile(src_video_path, target_video_path)

        if not os.path.exists(target_video_audio_path):
            # moviepy_utils.merge(target_video_path, target_audio_path, target_video_audio_path)
            ffmpeg_utils.merge(target_video_path, target_audio_path, target_video_audio_path)

        f = open(json_name, 'rb')
        json_content = f.read()
        f.close()
        json_content = str(json_content.decode("utf-8").replace('\'', '_'))
        print(json_content)
        j = json.loads(json_content)
        title = j.get('title').replace('__', '_').replace('❤', '').replace('͡', '')\
            .replace('ʖ', '').replace('°', '').replace('͜', '')\
            .replace('|', '').replace('(', '').replace(')', '').replace('\\', '')\
            .replace('/', '').replace('"', '').replace('?', '').replace('*', '')\
            .replace('，', '').replace('~', '').replace('>', '').replace('<', '')\
            .replace('！', '').replace('!', '').replace('？', '').replace(' ', '_')
        if j.get('page_data') and j.get('page_data').get('part'):
            part = j.get('page_data').get('part').replace('__', '_').replace('❤', '').replace('͡', '')\
                .replace('ʖ', '').replace('°', '').replace('͜', '')\
                .replace('|', '').replace('(', '').replace(')', '').replace('\\', '')\
                .replace('/', '').replace('"', '').replace('?', '').replace('*', '')\
                .replace('，', '').replace('~', '').replace('>', '').replace('<', '')\
                .replace('！', '').replace('!', '').replace('？', '').replace(' ', '_')
        else:
            part = ''

        if title == part:
            target_name = title + '_' + file_path_contents[-3] + '.mp4'
        else:
            target_name = title + '_' + part + file_path_contents[-3] + '.mp4'
        print(target_name)
        target_path = det_bili_path + os.path.sep + target_name

        if not os.path.exists(target_path):
            shutil.copyfile(target_video_audio_path, target_path)
