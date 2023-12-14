import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Path to the folder containing your original clips
original_folder_path = 'clips'

# Path to the folder where you want to save the new clips
new_folder_path = 'backgrounds'

# Get a list of all video files in the original folder
video_files = [file for file in os.listdir(original_folder_path) if file.endswith('.mp4')]

# Ensure the new folder exists, create it if not
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Create 100 random 15-second clips without duplicates
for i in range(100):
    # Choose random clips from the original folder without duplicates
    selected_clips = random.sample(video_files, k=5)  # Randomly select 3 clips without duplicates
    
    # Load the selected clips and filter by duration
    clips = []
    total_duration = 0
    for clip in selected_clips:
        video_path = os.path.join(original_folder_path, clip)
        current_clip = VideoFileClip(video_path)
        remaining_duration = 15 - total_duration
        
        if remaining_duration >= current_clip.duration:
            clips.append(current_clip)
            total_duration += current_clip.duration
        else:
            clips.append(current_clip.subclip(0, remaining_duration))
            total_duration = 15  # Update total duration to exit the loop
            break
    
    # Concatenate the clips
    final_clip = concatenate_videoclips(clips)
    
    # Pad the clip to make it exactly 15 seconds
    final_duration = final_clip.duration
    if final_duration < 15:
        padding = VideoFileClip(video_path).subclip(0, 15 - final_duration)
        final_clip = concatenate_videoclips([final_clip, padding])
    
    # Write the new clip to the new folder
    final_clip.write_videofile(
        os.path.join(new_folder_path, f'clip_{i + 1}.mp4'),
        codec='libx264',
        audio_codec='aac'  # Adding audio codec for better compatibility
    )
    
    # Close the clips to release memory
    final_clip.close()
    for clip in clips:
        clip.close()
