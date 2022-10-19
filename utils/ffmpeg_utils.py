import ffmpeg


def merge(video_path, audio_path, target_path):
    input_video = ffmpeg.input(video_path)
    input_audio = ffmpeg.input(audio_path)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(target_path).run()
