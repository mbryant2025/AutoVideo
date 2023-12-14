from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip

def add_images(fname1, fname2, output_name, video):
    video = VideoFileClip(video)
    # Load the images
    start_time_1 = 8.0
    start_time_2 = 8.7
    clip1 = ImageClip(fname1).set_start(start_time_1).set_duration(15 - start_time_1)
    clip2 = ImageClip(fname2).set_start(start_time_2).set_duration(15 - start_time_2)
    
    # Adjust image positions and resize them to fit 9:16 aspect ratio
    clip1 = clip1.set_position(("center", "top")).resize(width=video.w/4, height=int(video.w * 16 / 9)/4)
    clip2 = clip2.set_position(("center", "bottom")).resize(width=video.w/4, height=int(video.w * 16 / 9)/4)
    
    # Create the final composite video
    final = CompositeVideoClip([video, clip1, clip2], size=video.size)

    # Resize the final video to 9:16 aspect ratio
    final = final.resize(width=int(video.w * 9 / 16), height=video.h)

    # Write the final video
    final.write_videofile(output_name, fps=video.fps)

def main():
    add_images("images/arizona.jpg", "images/atlanta.jpg", "output.mp4", "video.mp4")

if __name__ == '__main__':
    main()

