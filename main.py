from extract_audio import extract_audio
from speech_to_text import speech_to_text
from translate import translate_text
from tts import text_to_speech
from merge import merge_audio_video

video_path = "input.mp4"

audio = extract_audio(video_path)
text = speech_to_text(audio)

print("Original Text:", text)

translated = translate_text(text)
print("Translated Text:", translated)

tts_audio = text_to_speech(translated)

final_video = merge_audio_video(video_path, tts_audio)

print("Done! Output saved as:", final_video)