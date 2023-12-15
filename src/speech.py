from gtts import gTTS 


def speech(text, fname="speech"):
  
    language = 'en'
  
    myobj = gTTS(text=text, lang=language, slow=False) 
   
    myobj.save(f"speech/{fname}.mp3")
  

def main():
    speech("This is the most epic Minecraft shot you'll ever see", "omaba")


if __name__ == '__main__':
    main()