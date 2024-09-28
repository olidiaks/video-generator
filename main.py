import moviepy.editor as mp
import os
from gtts import gTTS
import re

os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"

def generate_video(text):
    try:
        lang = 'pl'
        font_color = 'green'
        background_color = 'black'
        background_opacity =  1.0  # Default opacity is 1.0 (no transparency)
        font_size = 70  # Default font size is 70
        text_speed = 0.5  # Default text speed (adjust as needed)
        background_image_path = ''  # Path to background image (optional)

        # Generate voiceover using gTTS with the specified voice
        tts = gTTS(text=text, lang=lang)
        tts.save('voiceover.mp3')
        print("Voiceover generated")

        # Split the text into sentences using commas (',') and punctuation
        sentences = re.split(r'[.,!?]', text)

        # Create a list to store TextClips for each sentence
        sentence_clips = []

        # Calculate the duration for each sentence based on audio duration
        audio_duration = mp.AudioFileClip('voiceover.mp3').duration
        sentence_duration = audio_duration / len(sentences)

        current_time = 0

        for sentence in sentences:
            # Skip empty sentences
            if not sentence.strip():
                continue

            # Create a TextClip centered on the screen
            if background_image_path:
                # Load the background image and resize it to match the text clip size
                bg_image = mp.ImageClip(background_image_path)
                bg_image = bg_image.resize(size=(1500, 1000))  # Adjust the size as needed

                # Create a TextClip with background image
                word_clip = mp.TextClip(
                    sentence.strip(),
                    fontsize=font_size,
                    color=font_color,
                    bg_color=background_color,
                    size=(1500, 1000)
                )
                word_clip = word_clip.set_duration(sentence_duration)
                word_clip = word_clip.set_start(current_time)

                # Create a semi-transparent background color clip
                bg_color_clip = mp.ColorClip(
                    size=(1500, 1000),
                    color=background_color,
                    duration=sentence_duration,
                    is_mask=True,
                    opacity=background_opacity
                )

                # Composite the background color clip, background image, and text clip
                sentence_clip = mp.CompositeVideoClip([bg_color_clip, bg_image.set_duration(sentence_duration), word_clip])
            else:
                # Create a TextClip without background image
                sentence_clip = mp.TextClip(
                    sentence.strip(),
                    fontsize=font_size,
                    color=font_color,
                    bg_color=background_color,
                    size=(1500, 1000)
                )
                sentence_clip = sentence_clip.set_duration(sentence_duration)
                sentence_clip = sentence_clip.set_start(current_time)

            sentence_clips.append(sentence_clip)
            current_time += sentence_duration

        # Create a final CompositeVideoClip for all sentences
        text_clip = mp.concatenate_videoclips(sentence_clips, method="compose")

        # Create an audio clip from the generated voiceover
        audio_clip = mp.AudioFileClip('voiceover.mp3')

        # Set the audio for the text clip
        text_clip = text_clip.set_audio(audio_clip)

        # Set the duration for the text clip (same as audio duration)
        text_clip = text_clip.set_duration(audio_duration)

        # Set the fps for the text clip (e.g., 24 fps)
        text_clip = text_clip.set_fps(24)  # Adjust the value as needed

        # Define the directory for saving the video file
        output_directory = 'VSL'
        os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists

        # Write the video file using moviepy
        video_output_path = os.path.join(output_directory, 'voiceover_output.mp4')
        text_clip.write_videofile(video_output_path, codec='libx264', audio_codec='aac')
        print("Video generated")

        # Clean up temporary files
        os.remove('voiceover.mp3')
        print("Temporary files cleaned up")

        # Return the generated video file path

    except Exception as e:
        error_message = f'Error: {e}'
        print(error_message)  # Log the specific error message

generate_video("""
Rozprawka na temat: Dlaczego Linux jest lepszy niż Windows

W dzisiejszym świecie technologii operacyjny system komputerowy odgrywa kluczową rolę w codziennym użytkowaniu urządzeń. Wśród najpopularniejszych systemów operacyjnych wyróżniają się dwa dominujące: Linux i Windows. Choć każdy z nich ma swoje zalety i wady, wiele argumentów wskazuje, że Linux jest lepszym wyborem niż Windows.

Po pierwsze, jednym z najważniejszych atutów systemu Linux jest jego otwartość. Linux jest systemem typu open source, co oznacza, że jego kod źródłowy jest dostępny dla każdego. Dzięki temu programiści z całego świata mogą wprowadzać poprawki, rozwijać nowe funkcje i dostosowywać system do swoich potrzeb. To sprzyja innowacjom i przyspiesza rozwój oprogramowania. W przeciwieństwie do tego, Windows jest systemem zamkniętym, co ogranicza możliwości jego modyfikacji i dostosowywania.

Kolejnym argumentem na rzecz Linuxa jest jego bezpieczeństwo. Ze względu na swoją architekturę oraz fakt, że jest mniej popularny niż Windows, Linux jest mniej narażony na ataki złośliwego oprogramowania i wirusów. Systemy Linux mają wbudowane mechanizmy ochrony, a także regularne aktualizacje, które pozwalają na eliminację ewentualnych luk bezpieczeństwa. Użytkownicy systemu Windows często muszą zmagać się z problemami związanymi z wirusami i złośliwym oprogramowaniem, co może prowadzić do utraty danych i problemów z wydajnością.

Dodatkowo, Linux oferuje lepszą wydajność na starszym sprzęcie. Wiele dystrybucji Linuxa, takich jak Ubuntu, Fedora czy Mint, zostało zoptymalizowanych tak, aby działały płynnie nawet na komputerach o ograniczonych zasobach. Użytkownicy, którzy nie chcą inwestować w nowy sprzęt, mogą z powodzeniem korzystać z Linuxa na starszych maszynach, co nie zawsze jest możliwe w przypadku Windows.

Nie można także pominąć aspektu kosztów. Linux jest dostępny za darmo, co sprawia, że jest atrakcyjną opcją zarówno dla użytkowników indywidualnych, jak i firm. W przeciwieństwie do tego, licencje na system Windows są kosztowne i mogą stanowić znaczną część budżetu dla wielu użytkowników. Korzystanie z Linuxa pozwala zaoszczędzić pieniądze, które można przeznaczyć na inne aspekty działalności.

Podsumowując, istnieje wiele powodów, dla których Linux może być uważany za lepszy system operacyjny niż Windows. Otwartość kodu źródłowego, lepsze bezpieczeństwo, wydajność na starszym sprzęcie oraz brak kosztów związanych z licencjonowaniem to tylko niektóre z nich. Choć wybór systemu operacyjnego jest subiektywny i zależy od indywidualnych potrzeb użytkowników, Linux bez wątpienia zasługuje na uwagę i uznanie.
""")
