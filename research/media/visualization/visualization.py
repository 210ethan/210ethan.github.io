from openai import OpenAI
client = OpenAI()

def transcribe():
    
    # reference https://platform.openai.com/docs/guides/speech-to-text

    # specify audio file location
    audio_file = open("/Users/EthanMorse/Downloads/conversation.m4a", "rb")
    print("1")
    # transcribe using OpenAI's Whisper model
    # return transcript as string format
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text")
    
    print("2")

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

    summary = response['choices'][0]['message']['content']
    print("3")
    print (summary)
    
    return summary

def image(summary):
    
    # reference https://platform.openai.com/docs/guides/images

    print("4")
    # generate image based on gpt summary
    response = client.images.generate(
      model="dall-e-3",
      prompt=summary,
      size="1024x1024",
      quality="standard",
      n=1,)

    image_url = response.data[0].url
    print("5")

    return image_url

def main():

    transcript = transcribe()

    summary = summarize(transcript)

    image = image(summary)
    
main()
