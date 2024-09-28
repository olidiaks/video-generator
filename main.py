from moviepy.editor import TextClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip
from gtts import gTTS
from pydub import AudioSegment
import os


text = """
Buty są nieodłącznym elementem naszego codziennego życia. Niezależnie od tego, czy idziemy do pracy, szkoły, czy po prostu na spacer, odpowiednie buty mają ogromne znaczenie. Ale czy kiedykolwiek zastanawiałeś się, jak buty zmieniały się na przestrzeni wieków?

Pierwsze buty powstały tysiące lat temu. Były to proste kawałki skóry, które miały za zadanie chronić stopy przed trudnym terenem. W miarę rozwoju cywilizacji, buty zaczęły nabierać bardziej złożonych form. W starożytnym Egipcie noszono sandały wykonane z papirusu, które stały się symbolem statusu. W Rzymie legioniści maszerowali w solidnych, skórzanych butach, które chroniły ich podczas długich marszów.

W średniowieczu buty stały się bardziej ozdobne. Wysokie, szpiczaste buty, zwane poulaines, były popularne wśród europejskiej szlachty. Były one niepraktyczne, ale symbolizowały bogactwo i pozycję społeczną. Im dłuższy czubek buta, tym wyższy status właściciela.

Jednak to dopiero w XVIII i XIX wieku buty zaczęły przybierać formy, które są nam dziś bardziej znane. Wynalazek maszyn do szycia zrewolucjonizował produkcję obuwia, umożliwiając masową produkcję i dostępność dla szerszej publiczności. Buty stały się bardziej zróżnicowane pod względem stylu, koloru i funkcji.

Współczesne buty to prawdziwe arcydzieła inżynierii i mody. Mamy buty do biegania, buty na specjalne okazje, buty trekkingowe, a także buty codzienne. Każda para butów ma swoje specyficzne zastosowanie. Buty sportowe, takie jak te produkowane przez marki jak Nike czy Adidas, są wynikiem lat badań nad ergonomią, komfortem i wydajnością.

Moda na buty stale się zmienia. W ostatnich latach popularne stały się buty minimalistyczne, które mają na celu naśladowanie naturalnego ruchu stopy. Z drugiej strony, sneakersy stały się częścią popkultury, z limitowanymi edycjami osiągającymi ceny rzędu tysięcy dolarów.

Nie można też zapomnieć o wpływie, jaki mają buty na nasze zdrowie. Dobrze dobrana para butów może znacząco poprawić komfort codziennego życia, podczas gdy źle dobrane buty mogą prowadzić do problemów zdrowotnych, takich jak bóle kręgosłupa czy problemy z postawą.

Podsumowując, buty to nie tylko część garderoby, ale także ważny element naszej historii i kultury. To, jakie buty wybieramy, mówi wiele o nas samych, naszej osobowości i stylu życia. Dlatego warto zwrócić uwagę na jakość i dopasowanie obuwia, ponieważ to one wspierają nas na każdym kroku.
"""

def generate_audio(text, filename="narration.mp3"):
    tts = gTTS(text, lang='pl')
    tts.save(filename)

    # Konwertuj MP3 na WAV
    audio = AudioSegment.from_mp3("narration.mp3")
    audio.export("narration.wav", format="wav")

def generate_video_with_audio(text, output_filename="filmik_z_lektorem.mp4"):
    # Generowanie narracji audio
    generate_audio(text)
    
    # Dzielimy tekst na linijki i generujemy osobne klipy tekstowe
    lines = text.split(". ")
    video_clips = []
    total_duration = 0

    for line in lines:
        # Długość wyświetlania tekstu zależna od długości linii (3 sekundy na linijkę jako przykład)
        duration = max(3, len(line))  # np. 3 sekundy minimalnie, 0.1 sekundy na znak
        text_clip = TextClip(line, fontsize=50, color='green', size=(1280, 720), bg_color='black', method='caption').set_duration(duration)
        video_clips.append(text_clip)
        total_duration += duration

    # Połączenie wszystkich klipów tekstowych w jeden
    final_video = concatenate_videoclips(video_clips)

    # Dodanie audio do wideo
    audio = AudioFileClip("narration.wav").subclip(0, total_duration)
    final_video = final_video.set_audio(audio)

    # Zapisanie do pliku
    final_video.write_videofile(output_filename, fps=24)

# Przykład użycia
generate_video_with_audio(text, output_filename="filmik_z_lektorem.mp4")
