import wave
import sys
import pyaudio

import requests

import time

from PIL import Image

#import tkinter
#from PIL import ImageTk

from openai import OpenAI
client = OpenAI()


"""

image urls:
    - https://oaidalleapiprodscus.blob.core.windows.net/private/org-B7Jwzy0lMeAsxYwFNtVvZxMV/user-dttOoYdfOPxfpAA38uYOLf73/img-WRX171bmiNMYh3OEkcpPkjnA.png?st=2023-11-11T17%3A02%3A56Z&se=2023-11-11T19%3A02%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-11T09%3A22%3A33Z&ske=2023-11-12T09%3A22%3A33Z&sks=b&skv=2021-08-06&sig=kmGDg/PEaYrFrsZLxDoRWFE5Q/CFM1XwEK13c5z77Jc%3D
      img-WRX171bmiNMYh3OEkcpPkjnA.png
    - https://oaidalleapiprodscus.blob.core.windows.net/private/org-B7Jwzy0lMeAsxYwFNtVvZxMV/user-dttOoYdfOPxfpAA38uYOLf73/img-svFbh2K3anoNacNnvesjjRta.png?st=2023-11-14T01%3A33%3A56Z&se=2023-11-14T03%3A33%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-13T17%3A04%3A51Z&ske=2023-11-14T17%3A04%3A51Z&sks=b&skv=2021-08-06&sig=JFhmhLCPfWv3eV/CEY5C%2BMBF3FoXwyuTbJXCKGzgyZU%3D
    
todo:
    - put main() subfunctions in X min while loop
    - display image on full screen

"""


def record():
    
    # reference https://thepythoncode.com/article/play-and-record-audio-sound-in-python
    # reference https://people.csail.mit.edu/hubert/pyaudio/docs/
    # reference https://stackoverflow.com/questions/57940639/cannot-access-microphone-on-mac-mojave-using-pyaudio
    
    # the file name output you want to record into
    audio_file = "conversation.wav"
    
    # set the chunk size of 1024 samples
    chunk = 1024
    
    # sample format
    FORMAT = pyaudio.paInt16
    
    # mono, change to 2 if you want stereo
    channels = 1
    
    # 44100 samples per second
    sample_rate = 44100
    
    # how long to record for
    record_seconds = 60
    
    # initialize PyAudio object
    # When you set input=True in the p.open() method you will be able to use stream.read() to read from the microphone
    # also, when you set output=True, you'll be able to use stream.write() to write to the speaker
    p = pyaudio.PyAudio()
    
    print("----------------------record device list---------------------")
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk,
                    input_device_index=0)
    
    frames = []
    
    print("Recording...")
    
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
        
    print("Finished recording.")
    
    # stop and close stream
    stream.stop_stream()
    stream.close()
    
    # terminate pyaudio object
    p.terminate()
    
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(audio_file, "wb")
    
    # set the channels
    wf.setnchannels(channels)
    
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    
    # set the sample rate
    wf.setframerate(sample_rate)
    
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    
    # close the file
    wf.close()
    

def transcribe():
    
    # reference https://platform.openai.com/docs/guides/speech-to-text

    # specify audio file location
    audio_file = open("conversation.wav", "rb")

    # transcribe using OpenAI's Whisper model
    # return transcript as string format
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text")

    print (transcript)
    
    return transcript


def summarize(transcript):
    
    # reference https://platform.openai.com/docs/guides/text-generation/chat-completions-api

    # what to ask gpt
    request = "summarize this conversation: " + transcript

    # summarize transcript
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": request}])

    summary = response.choices[0].message.content

    print (summary)
    
    return summary


def image(summary):
    
    # reference https://platform.openai.com/docs/guides/images

    # generate image based on gpt summary
    response = client.images.generate(
      model="dall-e-3",
      prompt=summary,
      size="1024x1024",
      quality="standard",
      n=1,)

    image_url = response.data[0].url
    print(image_url)

    return image_url


def save(image_url):
    
    response = requests.get(image_url)
    
    with open("conversation.png", "wb") as f:
        f.write(response.content)
        
    time.sleep(5)
        

def display():
    
    picture = Image.open("conversation.png")
    
    picture.show()
    
    """
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = picture.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        picture = picture.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(picture)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()
    """

def main():
    
    # record conversation
    record()

    # transcribe conversation
    transcript = transcribe()

    # summarize conversation
    summary = summarize(transcript)
    
    # generate image of conversation
    image_url = image(summary)
    
    # save image of conversation
    save(image_url)
    
    # display image of conversation
    display()
    
    
"""
def main():
    
    while(True):
    
        # record conversation
        record()
    
        # transcribe conversation
        transcript = transcribe()
    
        # summarize conversation
        summary = summarize(transcript)
        
        # generate image of conversation
        image_url = image(summary)
        
        picture = save(image_url)
        
        display(picture)
        
        time.sleep(300)
"""
    
main()
