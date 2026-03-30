from gtts import gTTS

def text_to_speech(text, output_audio="output.mp3"):
    tts = gTTS(text, lang='kn')
    tts.save(output_audio)
    return output_audio