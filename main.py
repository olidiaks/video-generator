import os

from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip


# Funkcja do generowania mowy z tekstu za pomocą gTTS
def generate_audio(text, filename="audio.mp3", lang="pl"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return filename


# Funkcja do tworzenia filmu z tekstem i dźwiękiem
def generate_video_with_audio(text, output_filename="output.mp4"):
    # Generowanie ścieżki audio z tekstu
    audio_filename = generate_audio(text)

    # Tworzenie klipu wideo z napisem
    text_clip = TextClip(text, fontsize=70, color='white', size=(1280, 720), bg_color='black', method='caption')
    text_clip = text_clip.set_duration(10)  # Ustawienie długości klipu (dopasowanie do długości dźwięku)

    # Ładowanie ścieżki dźwiękowej
    audio_clip = AudioFileClip(audio_filename)
    text_clip = text_clip.set_audio(audio_clip)

    # Eksportowanie wideo
    text_clip.write_videofile(output_filename, fps=24, codec='libx264', audio_codec='aac')

    # Czyszczenie pliku audio po wygenerowaniu filmu
    if os.path.exists(audio_filename):
        os.remove(audio_filename)


# Przykładowy tekst do wygenerowania
text = "Witaj! To jest przykładowy tekst czytany przez lektora."

# Wywołanie funkcji do generowania filmu
generate_video_with_audio(text, output_filename="filmik_z_lektorem.mp4")
