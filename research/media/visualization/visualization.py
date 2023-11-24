import wave
import pyaudio

import requests

import time

from PIL import Image
import pyautogui

from openai import OpenAI
client = OpenAI()


"""

todo:
    - display image on full screen

"""


def record(length):

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
    record_seconds = length

    # initialize PyAudio object
    # When you set input=True in the p.open() method you will be able to use stream.read() to read from the microphone
    # also, when you set output=True, you'll be able to use stream.write() to write to the speaker
    p = pyaudio.PyAudio()

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
    # return transcript as string/text format
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

    # extract summary
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

    # extract image url
    image_url = response.data[0].url

    print(image_url)

    return image_url


def save(image_url, num_pics):

    # open image
    response = requests.get(image_url)

    # set file name based on how many images have been generated
    file_name = "conversation" + str(num_pics) + ".png"

    # save picture as file_name in folder
    with open(file_name, "wb") as f:
        f.write(response.content)

    # wait five seconds to allow for saving
    time.sleep(5)

    return file_name


def display(file_name):

    # open and display image
    picture = Image.open(file_name)
    picture.show()

    # wait five seconds to let the picture come up
    time.sleep(5)

    # click to maximize window to full screen
    pyautogui.click(70, 56)


def main():

    # how long to record for
    length = 45

    # how long to display image for
    display_time = 240

    # index 1 for number of pictures
    num_pics = 1

    while(True):

        # record conversation
        record(length)

        # transcribe conversation
        transcript = transcribe()

        # summarize conversation
        summary = summarize(transcript)

        # generate image of conversation
        image_url = image(summary)

        # save image of conversation
        file_name = save(image_url, num_pics)

        # display image of conversation
        display(file_name)

        # iterate so no overwriting until next sessions
        num_pics += 1

        # wait 9 min before next pic
        time.sleep(display_time)


main()
