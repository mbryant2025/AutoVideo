from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bing_images import bing
import os

# driver = webdriver.Chrome(ChromeDriverManager().install())


def download(query):

    # Make a folder called images_temp
    if not os.path.exists("images_temp"):
        os.mkdir("images_temp")

    bing.download_images(query + " skyline",
                        1,
                        output_dir="images_temp",
                        pool_size=1,
                        force_replace=True)
    

    # Move everything from imageds_temp to images
    for filename in os.listdir("images_temp"):
        # Format the filename by first removing all underscores, then replace all spaces with underscores, then remove all numbers
        new_filename = (query.replace(" ", "_") + ".jpg").lower()
        os.rename(f"images_temp/{filename}", f"images/{new_filename}")
        break

    # Clear the images_temp folder
    for filename in os.listdir("images_temp"):
        os.remove(f"images_temp/{filename}")

    os.rmdir("images_temp")

    
def main():
    download("new york city")


if __name__ == '__main__':
    main()
