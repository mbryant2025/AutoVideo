# Cut the video to be exactly 15 seconds long while keeping the audio intact

from moviepy.editor import VideoFileClip

def cut_video(video, output_name):
    video = VideoFileClip(video)
    video = video.subclip(0, 15)
    video.write_videofile(output_name, codec='libx264', audio_codec='aac')
