import os
import random

from src.load_images import download
from src.pick_populations import get_random_rows
from src.speech import speech
from src.overlay_photo import add_images
from src.video_text import add_text
from src.overlay_speech import add_speech
from src.cut_video import cut_video
from src.combine_audio import combine_audio


def main():

    # Pick two random population areas
    result = get_random_rows()

    city_1 = result[0][0][1]
    city_2 = result[1][0][1]

    city_1_formatted = city_1.replace(" ", "_").lower()
    city_2_formatted = city_2.replace(" ", "_").lower()

    # Check if there are images for both cities/states
    # If there aren't, download them

    if not os.path.exists(f"images/{city_1_formatted}.jpg"):
        download(city_1)

    if not os.path.exists(f"images/{city_2_formatted}.jpg"):
        download(city_2)

    # Make the temp_video folder
    if not os.path.exists("temp_video"):
        os.mkdir("temp_video")

    # Generate the speech

    # Nuke the temp_video folder
    # for filename in os.listdir("temp_video"):
    #     os.remove(f"temp_video/{filename}")

    default_question = "9 out of 10 people can't answer this U.S population question, can you?"
    
    # If we already have a default speech file, use that
    if not os.path.exists("speech/question.mp3"):
        speech(default_question, "question")

    specific_question = f"Which has a larger population? {city_1} or {city_2}?"

    speech(specific_question, "question_specific")

    answer = f"The answer is {city_1 if int(result[0][1][1]) > int(result[1][1][1]) else city_2}! "

    speech(answer, "answer")

    # Add the text to the video
    # Saves in video/text.mp4
    
    # Start with the default question

    city_1_population = result[0][1][1]
    city_2_population = result[1][1][1]

    text_times = [
        ("9 out of 10 people", 0.2),
        ("can't answer this", 1.4),
        ("U.S. population question", 2.2),
        ("Can you?", 4.3),
        ("Which has a ", 5.5),
        ("larger population?", 6.0),
        (f"{city_1} or {city_2}?", 8.0),
        # Indicator of answer
        (f"{city_1}_{city_1_population}_{city_2}_{city_2_population}", 14.0),
    ]

    # Choose random file from backgrounds folder
    empty_video = "backgrounds/" + random.choice(os.listdir("backgrounds"))

    video_input = "temp_video/a.mp4"
    video_output = "temp_video/b.mp4"

    final_video = f"video/{city_1_formatted}_{city_2_formatted}.mp4"

    # Cut the video to 15 seconds and output to video/video.mp4
    cut_video(video=empty_video, output_name=video_output)
    video_input, video_output = video_output, video_input

    add_text(text_info=text_times, fname=video_input, output_name=video_output)
    video_input, video_output = video_output, video_input

    # Add the images to the video and output to temp_video/pictures.mp4
    add_images(fname1=f"images/{city_1_formatted}.jpg", fname2=f"images/{city_2_formatted}.jpg", output_name=video_output, video=video_input)
    video_input, video_output = video_output, video_input

    # Combine the speech into one speech file called speech/speech.mp3
    # def combine_audio(audio_files, start_times, output_name):
    combine_audio(["speech/question.mp3", "speech/question_specific.mp3", "speech/answer.mp3"], [0, 5.3, 13], "speech/speech.mp3")

    # Add speech to the video and output to temp_video/question.mp4
    add_speech(video_path=video_input, audio_path="speech/speech.mp3", output_name=final_video)

    # Nuke the temp_video folder
    for filename in os.listdir("temp_video"):
        os.remove(f"temp_video/{filename}")

    # Remove the folder itself
    os.rmdir("temp_video")

    # Remove speech/sppech.mp3 and speech/question_specific.mp3 and speech/anwser.mp3
    os.remove("speech/speech.mp3")
    os.remove("speech/question_specific.mp3")
    os.remove("speech/answer.mp3")


if __name__ == '__main__':
    while 1:

        try:
            main()
        except:
            pass
    