from gtts import gTTS
from moviepy.editor import *
import os
import threading
import re

text = """
Po pierwsze, jednym z najważniejszych atutów systemu Linux jest jego otwartość. Linux jest systemem typu open source, co oznacza, że jego kod źródłowy jest dostępny dla każdego. Dzięki temu programiści z całego świata mogą wprowadzać poprawki, rozwijać nowe funkcje i dostosowywać system do swoich potrzeb. To sprzyja innowacjom i przyspiesza rozwój oprogramowania. W przeciwieństwie do tego, Windows jest systemem zamkniętym, co ogranicza możliwości jego modyfikacji i dostosowywania.
"""

# Funkcja do generowania plików audio
def generate_audio(text, index):
    tts = gTTS(text, lang='pl')  # język polski
    audio_file = f"audio_{index}.mp3"
    tts.save(audio_file)
    return audio_file

# Funkcja do tworzenia klipu wideo z napisami
def create_video_with_subtitle(audio_file, text, index):
    # Ustal długość klipu na podstawie długości audio
    audio_clip = AudioFileClip(audio_file)
    duration = audio_clip.duration
    
    # Tworzymy pusty wideo klip o czarnym tle
    video_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=duration)
    
    # Dodajemy napisy do klipu
    txt_clip = TextClip(text, fontsize=40, color='green', size=video_clip.size, method="caption", print_cmd=True)
    txt_clip = txt_clip.set_position('center').set_duration(duration)
    
    # Łączymy wideo i napisy
    video_with_subtitle = CompositeVideoClip([video_clip, txt_clip]).set_audio(audio_clip)
    
    # Eksportujemy klip
    video_with_subtitle_file = f"video_{index}.mp4"
    video_with_subtitle.write_videofile(video_with_subtitle_file, fps=10)
    
    return video_with_subtitle_file

# Funkcja do łączenia plików wideo w całość
def combine_videos(video_files):
    clips = [VideoFileClip(vf) for vf in video_files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("final_video.mp4", fps=24)

# Dzielimy tekst na zdania
sentences = re.split(r'[.,!?]', text)
audio_files = []
video_files = []

# Generujemy audio i wideo dla każdego zdania
for i, sentence in enumerate(sentences):
    if sentence.strip():  # pomijamy puste zdania
        audio_file = generate_audio(sentence.strip(), i)
        audio_files.append(audio_file)
        
        video_file = create_video_with_subtitle(audio_file, sentence.strip(), i)
        video_files.append(video_file)
        
        print(f"Zdanie {i+1}: {sentence.strip()}")  # Wyświetlamy tekst na ekranie


# Łączymy pliki wideo w jeden
combine_videos(video_files)

# Usuwamy pliki tymczasowe
for audio_file in audio_files:
    os.remove(audio_file)
for video_file in video_files:
    os.remove(video_file)

print("Wszystkie klipy wideo zostały połączone w 'final_video.mp4'")
