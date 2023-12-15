import cv2


def add_text(text_info, fname, output_name="temp_video/text.mp4"):

    cap = cv2.VideoCapture(fname)

    # Get the video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_name, fourcc, fps, (width, height))

    current_text = ""
    text_index = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        vid_height, vid_width, _ = frame.shape

        font = cv2.FONT_HERSHEY_SIMPLEX

        # Calculate elapsed time in seconds
        elapsed_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

        if text_index < len(text_info):
            text, display_time = text_info[text_index]
            if elapsed_time >= display_time:
                current_text = text
                text_index += 1

        if current_text:
           

            # If there are any numbers in the text, this is our answer
            if any(char.isdigit() for char in current_text) and current_text != "9 out of 10 people":
                # Split by underscores
                split_text = current_text.split("_")

                # It goes city_1, city_1_population, city_2, city_2_population
                city_1 = split_text[0]
                city_1_population = split_text[1]
                city_2 = split_text[2]
                city_2_population = split_text[3]


                # Format the populations with commas
                city_1_population_commas = "{:,}".format(int(city_1_population))
                city_2_population_commas = "{:,}".format(int(city_2_population))

                # Add the text to the screen
                cv2.putText(frame,
                            city_1,
                            (int(vid_width / 2) - 200, int(vid_height / 2) - 300),
                            font, 2,
                            (255, 255, 255) if int(city_2_population) > int(city_1_population) else (0, 255, 0),
                            8,
                            cv2.LINE_4)
                
                cv2.putText(frame,
                            city_2,
                            (int(vid_width / 2) - 200, int(vid_height / 2) + 300),
                            font, 2,
                            (255, 255, 255) if int(city_1_population) > int(city_2_population) else (0, 255, 0),
                            8,
                            cv2.LINE_4)
                
                # Add the or to the screen

                cv2.putText(frame,
                            "or",
                            (int(vid_width / 2) - 200, int(vid_height / 2)),
                            font, 2,
                            (255, 255, 255),
                            8,
                            cv2.LINE_4)
                
                # Add the population to the screen
                cv2.putText(frame,
                            city_1_population_commas,
                            (int(vid_width / 2) - 200, int(vid_height / 2) - 200),
                            font, 2,
                            (255, 255, 255) if int(city_2_population) > int(city_1_population) else (0, 255, 0),
                            8,
                            cv2.LINE_4)
                
                cv2.putText(frame,
                            city_2_population_commas,
                            (int(vid_width / 2) - 200, int(vid_height / 2) + 200),
                            font, 2,
                            (255, 255, 255) if int(city_1_population) > int(city_2_population) else (0, 255, 0),
                            8,
                            cv2.LINE_4)
                
            
             # If current_text contains "or", split it
            elif "or" in current_text:
                # Split by only the first "or"
                split_text = current_text.split("or", 1)
                cv2.putText(frame,
                            split_text[0],
                            (int(vid_width / 2) - 200, int(vid_height / 2) - 300),
                            font, 2,
                            (255, 255, 255),
                            8,
                            cv2.LINE_4)

                cv2.putText(frame,
                            split_text[1][1:],
                            (int(vid_width / 2) - 200, int(vid_height / 2) + 300),
                            font, 2,
                            (255, 255, 255),
                            8,
                            cv2.LINE_4)
                
                # Add the or to the screen
                cv2.putText(frame,
                            "or",
                            (int(vid_width / 2) - 100, int(vid_height / 2)),
                            font, 2,
                            (255, 255, 255),
                            8,
                            cv2.LINE_4)


            else:
                cv2.putText(frame,
                            current_text,
                            (int(vid_width / 2) - 400, int(vid_height / 2) - 100),
                            font, 2,
                            (255, 255, 255),
                            8,
                            cv2.LINE_4)

        # Write the modified frame to the output video
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything
    cap.release()
    out.release()


def main():
    # Specify text and display time as tuples: (text, display_time)
    # text_info = [
    #     ("Hello", 10),
    #     ("Michael or Jordan?", 12),
    #     ("Connecticut_56_New York_19", 14),
    # ]
    # add_text(text_info, "video.mp4")

    text_info = [
        ("This is the most epic", 0),
        ("Minecraft shot", 2),
        ("you'll ever see", 4),
    ]
    add_text(text_info, "epic_shot2.mp4", "epic_shot3.mp4")

if __name__ == '__main__':
    main()
