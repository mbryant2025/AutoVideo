from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def add_speech(video_path, audio_path, output_name, start_time=0):
    # Load the video and audio files
    video_clip = VideoFileClip(video_path)
    audio_clip_video = video_clip.audio

    # Check if the video has audio
    if audio_clip_video is not None:
        audio_clip_mp3 = AudioFileClip(audio_path)

        # Trim the audio from the mp3 to start at the specified time
        audio_clip_mp3 = audio_clip_mp3.set_start(start_time)

        # Mix the audio from both sources
        final_audio = CompositeAudioClip([audio_clip_video, audio_clip_mp3])

        # Set the composite audio to the video
        video_clip = video_clip.set_audio(final_audio)
    else:
        # If there's no audio in the video, use only the provided audio file
        video_clip = video_clip.set_audio(AudioFileClip(audio_path).set_start(start_time))

    # Write the output file
    video_clip.write_videofile(output_name, codec='libx264', audio_codec='aac')


def main():
    # add_speech("video.mp4", "speech/question.mp3", "temp_video/question.mp4")

    # add_speech("temp_video/question.mp4", "speech/question_specific.mp3", "temp_video/question2.mp4", start_time=5.5)

    # add_speech("temp_video/question2.mp4", "speech/answer.mp3", "temp_video/question3.mp4", start_time=12)

    add_speech("epic_shot.mov", "omaba.mp3", "epic_shot2.mp4", start_time=0)


if __name__ == '__main__':
    main()
