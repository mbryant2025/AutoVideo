from gtts import gTTS 


def speech(text, fname="speech"):
  
    language = 'en'
  
    myobj = gTTS(text=text, lang=language, slow=False) 
   
    myobj.save(f"speech/{fname}.mp3")
  

def main():
    speech("Connecticut is the motherland of pizza", "omaba")


if __name__ == '__main__':
    main()