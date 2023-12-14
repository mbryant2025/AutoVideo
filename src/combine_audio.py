from moviepy.editor import AudioFileClip, CompositeAudioClip


def combine_audio(audio_files, start_times, output_name):

    # Load the audio files
    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_files]

    # Adjust the start times for each audio clip
    adjusted_clips = []
    for clip, start_time in zip(audio_clips, start_times):
        adjusted_clip = clip.set_start(start_time)
        adjusted_clips.append(adjusted_clip)

    # Combine the adjusted audio clips
    final_audio = CompositeAudioClip(adjusted_clips)

    # Write the combined audio to a file
    final_audio.write_audiofile(output_name, fps=44100)  # Adjust FPS as needed


def main():
    combine_audio(
        ["speech/question.mp3", "speech/question_specific.mp3", "speech/answer.mp3"],
        [0, 5.5, 13],
        "speech.mp3"
    )
    
if __name__ == '__main__':
    main()
