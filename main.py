"""
Copytight (c) 2024 Oliwier Stępniak
This program will generate a video where text is displayed on the screen while it is read aloud. The text should be assigned to the text variable, and the language of the text should be specified by modifying the lang variable.

     This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

     This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

     You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA. Also add information on how to contact you by electronic and paper mail.
"""

from gtts import gTTS
from moviepy.editor import *
import os
import threading
import re

lang = 'pl'

text = """
ZASADA: KISS, DRY, YAGNI..
KISS - Keep It Simple, Stupid..
Kod powinien być jak najprostszy. Unikaj skomplikowanych rozwiązań, aby ułatwić zrozumienie i utrzymanie..
DRY - Don't Repeat Yourself..
Unikaj powtórzeń w kodzie. Zmiany wprowadza się łatwiej, a błędy łatwiej wykrywa, gdy kod jest zorganizowany w sposób, który minimalizuje duplikację.  .
YAGNI - You Aren't Gonna Need It,.
Nie twórz kodu "na zapas". Pisz tylko to, co jest potrzebne teraz, aby uniknąć zbędnych komplikacji w przyszłości. Te zasady pomagają w tworzeniu czytelnego i łatwego w utrzymaniu kodu. .
Metody projektowania algorytmu: Zasada Dziel i zwyciężaj, Lista kroków, Pseudokod. Drzewo decyzyjne, Schemat blokowy, Złożoność obliczeniowa.  .
Zasada Dziel i Zwyciężaj..
Polega na dzieleniu problemu na mniejsze podproblemy. Rozwiązania podproblemów są łączone, aby uzyskać rozwiązanie pierwotnego problemu.  .
Lista Kroków..
Precyzyjnie opisuje, co należy zrobić w każdym etapie algorytmu. Pomaga uniknąć nieporozumień w implementacji.  .
Pseudokod..
Przedstawia algorytm w formie zrozumiałej dla ludzi. Ułatwia zrozumienie logiki algorytmu przed implementacją.  .
Drzewo Decyzyjne..
Ilustruje decyzje i ich możliwe konsekwencje. Wizualizuje procesy decyzyjne w algorytmie.  .
Schemat Blokowy..
Graficzna reprezentacja algorytmu używająca kształtów do przedstawienia kroków procesu. Wizualizuje przepływ danych i logikę algorytmu.  .
Złożoność Obliczeniowa .
Odnosi się do ilości zasobów potrzebnych do wykonania algorytmu. Ocenia efektywność algorytmu. .
Wykorzystanie diagramu UML  w projektowaniu klas. Przykład.  .
UML (Unified Modeling Language) diagramy klasowe są niezbędnymi narzędziami w projektowaniu obiektowym, zapewniając wizualną reprezentację klas, ich atrybutów, metod oraz relacji między nimi. 
Wykorzystanie diagramu UML w projektowaniu klas .
Definicja klas .
Klasa w diagramie UML to szablon definiujący właściwości (atrybuty) i zachowania (metody) obiektów. Klasy są przedstawiane jako prostokąty podzielone na trzy sekcje: nazwę, atrybuty i operacje.  .
Typy relacji .
Diagramy UML pokazują różne typy relacji między klasami, takie jak asocjacja, agregacja, kompozycja, dziedziczenie i realizacja. Każdy typ relacji ma swoje znaczenie, na przykład asocjacja oznacza "używa", a kompozycja wskazuje na silne powiązanie, gdzie część nie może istnieć bez całości.  .
Przykład zastosowania .
Przykładem może być diagram przedstawiający klasę Samochód, która ma atrybuty takie jak marka i model, oraz metody takie jak przyspiesz(). Klasa Samochód może być powiązana z klasą Silnik poprzez relację agregacji, co oznacza, że samochód "ma" silnik, ale silnik może istnieć niezależnie od samochodu. .
Czym są wzorce projektowe Gangu Czworga?  .
Wzorce projektowe Gangu Czworga to zestaw 23 uniwersalnych rozwiązań dla powtarzających się problemów w projektowaniu oprogramowania, które zostały opisane w książce z 1995 roku. Dzielą się one na trzy główne kategorie: wzorce kreacyjne, strukturalne i behawioralne, co ułatwia ich zastosowanie w różnych kontekstach programistycznych. .
Wymień 4 elementy które musi mieć każdy wzorzec projektowy Gangu Czworga.  .
Każdy wzorzec projektowy Gangu Czworga składa się z czterech podstawowych elementów:  .
Nazwa wzorca .
Jednoznaczna nazwa wzorca ułatwia komunikację między osobami w zespole projektowym, wiedząc że każdy mówi o tym samym. Pozwala to również na łatwiejszą analizę dokumentacji i skrócenie fragmentów odpowiadających z danym wzorcem.  .
Opis problemu .
Określa kiedy dany wzorzec projektowy może być zastosowany. Czasami w opisie znajduje się algorytm lub lista warunków wymaganych do zaistnienia okoliczności których rozwiązanie opisuje wzorzec.  .
Rozwiązanie .
Opis elementów oraz relacji między nimi które pozwalają na szybkie i sprawdzone rozwiązanie opisywanego problemu. Rozwiązanie nie jest nigdy konkretnym projektem lub konkretną implementacją, a raczej szablonem do zastosowania.  .
Konsekwencje .
Opis jakie są zyski, koszty oraz oczekiwane efekty w momencie zastosowania wzorca. Dobrze opisane konsekwencje pozwalają na świadome podjęcie decyzji o wykorzystaniu danego wzorca. .
Wymień i opisz 3 grupy wzorców Gangu Czworga.  .
Wzorce projektowe Gangu Czworga dzielą się na trzy główne grupy:  .
Wzorce kreacyjne .
Te wzorce koncentrują się na procesie tworzenia obiektów. Umożliwiają one elastyczne zarządzanie inicjalizacją obiektów, co pozwala na ich łatwe dostosowanie do różnych potrzeb, np. poprzez wzorce takie jak Singleton, Fabryka Abstrakcyjna czy Budowniczy.  .
Wzorce strukturalne .
Wzorce strukturalne zajmują się organizacją i kompozycją obiektów, definiując relacje między nimi. Dzięki nim można tworzyć złożone struktury z prostszych elementów, co ułatwia zarządzanie kodem, przykłady to Adapter, Dekorator i Fasada.  .
Wzorce behawioralne .
Te wzorce koncentrują się na interakcjach i komunikacji między obiektami. Opisują, jak obiekty współdziałają ze sobą, co pozwala na lepsze zarządzanie ich zachowaniem, przykłady to Obserwator, Strategia i Komenda. .
Siedem zasad testowania oprogramowania.  .
Siedem zasad testowania oprogramowania to kluczowe wytyczne, które pomagają w zapewnieniu jakości i efektywności procesu testowania. Zostały one opracowane przez ISTQB (International Software Testing Qualifications Board) i stanowią fundament dla testerów oprogramowania. Oto szczegółowy opis każdej z zasad:  .
Testowanie ujawnia usterki, ale nie może dowieść ich braku .
 Testowanie ma na celu wykrycie błędów w oprogramowaniu, jednak nie jest w stanie potwierdzić, że oprogramowanie jest całkowicie wolne od defektów. Nawet jeśli testy nie ujawnią żadnych problemów, nie oznacza to, że ich nie ma .
Testowanie gruntowne jest niemożliwe .
 Nie można przetestować wszystkich możliwych kombinacji danych wejściowych i warunków wstępnych, szczególnie w złożonych systemach. Dlatego kluczowe jest skupienie się na najważniejszych elementach i ryzykach, zamiast próbować testować wszystko .
Wczesne testowanie oszczędza czas i pieniądze .
 Rozpoczęcie testowania na jak najwcześniejszym etapie cyklu życia oprogramowania pozwala na wcześniejsze wykrycie defektów, co przekłada się na oszczędności w czasie i kosztach. Wczesne testowanie jest często określane jako "przesunięcie w lewo" .
Kumulowanie się defektów .
 Wiele błędów w oprogramowaniu może występować w określonych obszarach lub modułach. Zasada ta odnosi się do obserwacji, że 20% modułów może odpowiadać za 80% wszystkich błędów, co skłania zespoły testerskie do skupienia się na tych krytycznych obszarach .
Paradoks pestycydów .
 Powtarzanie tych samych testów prowadzi do ich osłabienia w wykrywaniu nowych defektów. Podobnie jak w przypadku pestycydów, które przestają być skuteczne przy ciągłym używaniu, testy również wymagają odmiany i aktualizacji, aby były efektywne .
Testowanie zależy od kontekstu .
 Metody i podejścia do testowania powinny być dostosowane do specyfiki testowanego oprogramowania. Na przykład, aplikacje bankowe będą wymagały innego podejścia niż systemy e-commerce, co wynika z różnorodnych wymagań i priorytetów 
Przekonanie o braku błędów jest błędem 
 Utrzymywanie przekonania, że oprogramowanie jest wolne od błędów po przeprowadzeniu testów, jest niebezpieczne. Testowanie może znacznie zmniejszyć ryzyko błędów, ale nie może go całkowicie wyeliminować .
Te zasady stanowią fundament dla skutecznego testowania oprogramowania i pomagają w osiągnięciu wysokich standardów jakości. 
Co to jest ISTQB?  
ISTQB to skrót od International Software Testing Qualifications Board, czyli Międzynarodowej Rady Kwalifikacji w zakresie testowania oprogramowania, która jest organizacją non-profit założoną w 2002 roku. Oferuje program certyfikacji dla testerów oprogramowania, który jest uznawany na całym świecie i składa się z różnych poziomów, w tym podstawowego (Foundation Level) oraz zaawansowanego. 
7 czynności z których składa się proces testowy według ISTQB. 
Proces testowy według standardów ISTQB składa się z siedmiu kluczowych czynności:  
Planowanie testów - określenie strategii i zakresu testowania. 
Monitorowanie i nadzór nad testami - śledzenie postępów i jakości testów. 
Analiza testów - przegląd wymagań i specyfikacji w celu zrozumienia, co powinno być testowane. 
Projektowanie testów - tworzenie przypadków testowych i scenariuszy. 
Implementacja testów - przygotowanie środowiska testowego i narzędzi. 
Wykonanie testów - przeprowadzenie testów i zbieranie wyników. 
Finalizacja - ocena wyników testów i raportowanie. 
Co to są poziomy testów? Wymień je i opisz.(modułowe, integracyjne, systemowe, akceptacyjne) 
Poziomy testów w procesie wytwarzania oprogramowania są kluczowe dla zapewnienia jakości i funkcjonalności systemów. Wyróżnia się cztery podstawowe poziomy testowania: testy modułowe, testy integracyjne, testy systemowe oraz testy akceptacyjne. Każdy z tych poziomów ma swoje unikalne cele, metody oraz obszary zastosowania.  
Testy modułowe (jednostkowe) .
Opis: Testy modułowe są najniższym poziomem testowania, koncentrującym się na weryfikacji pojedynczych komponentów lub funkcji oprogramowania. Ich celem jest sprawdzenie, czy dany fragment kodu działa zgodnie z założeniami. Cele:  
Wyszukiwanie defektów w poszczególnych jednostkach kodu. 
Weryfikacja funkcjonalności modułów w izolacji. 
Przykłady: Testowanie funkcji przeliczającej waluty, gdzie sprawdza się, czy odpowiednie wartości są poprawnie przetwarzane.  
Testy integracyjne.
Opis: Testy integracyjne sprawdzają interakcje pomiędzy różnymi modułami lub systemami. Celem jest upewnienie się, że poszczególne części aplikacji współpracują ze sobą poprawnie. Cele:.
Weryfikacja interfejsów między modułami. 
Sprawdzenie poprawności współpracy różnych systemów i ich komponentów. 
Przykłady: Testowanie połączeń między bazą danych a aplikacją lub interakcje między mikrousługami.  
Testy systemowe.
Opis: Testy systemowe oceniają cały system jako całość, sprawdzając jego zgodność z wymaganiami funkcjonalnymi i niefunkcjonalnymi. Obejmuje to zarówno testy funkcjonalne, jak i wydajnościowe. Cele:  
Sprawdzenie, czy cały system działa zgodnie z wymaganiami biznesowymi. 
Ocena wydajności, bezpieczeństwa oraz stabilności systemu. 
Przykłady: Testowanie pełnych scenariuszy użytkowników, takich jak proces logowania czy zakupu produktu online.  
Testy akceptacyjne 
Opis: Testy akceptacyjne są przeprowadzane na końcowym etapie cyklu życia oprogramowania. Ich celem jest potwierdzenie, że system spełnia wymagania klienta i jest gotowy do wdrożenia. Cele:  
Upewnienie się, że oprogramowanie spełnia oczekiwania użytkowników końcowych. 
Walidacja systemu przed jego wdrożeniem do produkcji. 
Przykłady: Użytkownicy testują aplikację w rzeczywistych warunkach, aby ocenić jej użyteczność i funkcjonalność. Każdy z tych poziomów testowania odgrywa istotną rolę w zapewnieniu jakości oprogramowania i powinien być realizowany w odpowiednich fazach procesu rozwoju. 
Co to jest Re-test? 
Retest to proces testowania, który ma na celu potwierdzenie, że wcześniej zidentyfikowany błąd w oprogramowaniu został skutecznie naprawiony. W przeciwieństwie do testów regresyjnych, które sprawdzają, czy nowe zmiany nie wprowadziły nowych błędów w już działających funkcjonalności, retest koncentruje się wyłącznie na zweryfikowaniu konkretnego defektu. 
Wyjaśnij pojęcie testy regresywne. 
Testy regresywne to proces ponownego testowania oprogramowania po wprowadzeniu modyfikacji, mający na celu upewnienie się, że zmiany nie wprowadziły nowych defektów ani nie wpłynęły negatywnie na istniejące funkcjonalności. Celem tych testów jest identyfikacja potencjalnych problemów w kodzie, które mogłyby ujawnić się w wyniku aktualizacji lub zmian w środowisku pracy aplikacji. 
Typy testów, wymień i opisz.(funkcjonalne, niefunkcjonalne) 
Typy testów oprogramowania 
Testowanie oprogramowania można podzielić na dwa główne typy: testy funkcjonalne i testy niefunkcjonalne. Każdy z tych typów ma swoje specyficzne cele oraz metody, które są kluczowe dla zapewnienia jakości oprogramowania.  
Testy funkcjonalne 
Definicja: Testy funkcjonalne mają na celu weryfikację, czy system działa zgodnie z wymaganiami funkcjonalnymi. Obejmują one testowanie poszczególnych funkcji aplikacji oraz ich interakcji. Charakterystyka:  
Metoda testowania: Często określane jako testy "czarnej skrzynki", ponieważ testerzy nie muszą znać wewnętrznej struktury systemu. Skupiają się na tym, co system powinien robić, a nie jak to robi. 
Zakres: Testy te mogą być przeprowadzane na różnych poziomach, takich jak testy jednostkowe, integracyjne czy systemowe. 
Przykłady: Testowanie logiki biznesowej, walidacja danych wejściowych, testy przypadków użycia. 
Testy niefunkcjonalne 
Definicja: Testy niefunkcjonalne oceniają aspekty jakościowe systemu, które nie są bezpośrednio związane z jego funkcjonalnością. Skupiają się na tym, jak system działa w różnych warunkach. Charakterystyka:  
Metoda testowania: Nazywane również testami "jak działa" system. Wymagają one analizy wydajności, bezpieczeństwa i użyteczności aplikacji. 
Zakres: Testy niefunkcjonalne obejmują różnorodne kategorie, takie jak:  
Wydajność: Testy wydajnościowe, obciążeniowe i przeciążeniowe oceniają czas odpowiedzi i stabilność systemu pod różnymi obciążeniami. 
Bezpieczeństwo: Testowanie zabezpieczeń aplikacji przed atakami i naruszeniami danych. 
Użyteczność: Ocena interfejsu użytkownika i ogólnej ergonomii aplikacji. 
Niezawodność i utrzymywalność: Sprawdzanie, jak dobrze system radzi sobie z błędami i jak łatwo można go modyfikować w przyszłości. 
Jakie informacje powinno zawierać poprawne zgłoszenie błędu? 
Aby zgłoszenie błędu było poprawne i skuteczne, powinno zawierać: 
Unikalny identyfikator 
 Każde zgłoszenie powinno mieć swój unikalny identyfikator, co ułatwia późniejsze odniesienia do konkretnego błędu.  
 Tytuł powinien być krótki i precyzyjny, jasno wskazując na naturę błędu. Przykład: "Koszyk - nie działa usuwanie produktu".  
Opis 
 Opis powinien szczegółowo przedstawiać problem oraz kontekst, w którym występuje błąd. Powinien zawierać informacje o tym, co dokładnie się dzieje i jakich kroków użyto do jego odtworzenia.  
Kroki reprodukcji .
 Należy szczegółowo opisać, jak krok po kroku wywołać dany błąd. Każdy krok powinien być zapisany w osobnej linii, co ułatwia zrozumienie procesu.  
Oczekiwany vs. rzeczywisty wynik 
 Warto podać, jaki był oczekiwany rezultat działania aplikacji oraz co rzeczywiście się wydarzyło (np. "Oczekiwany wynik: strona załadowana; Rzeczywisty wynik: błąd 404").  
Środowisko .
 Informacje o środowisku, w którym występuje błąd (np. wersja oprogramowania, przeglądarka, system operacyjny), są kluczowe dla reprodukcji problemu.  
Priorytet zgłoszenia 
 Określenie priorytetu błędu pomaga zespołowi zdecydować, jak szybko powinien zostać naprawiony.  
Załączniki .
 Dodatkowe materiały takie jak zrzuty ekranu, nagrania wideo czy logi mogą znacznie pomóc w identyfikacji problemu.  
Informacje o zgłaszającym 
 Warto podać dane kontaktowe osoby zgłaszającej błąd, aby programiści mogli łatwo uzyskać dodatkowe informacje w razie potrzeby.  
Status zgłoszenia .
 Informacje o aktualnym statusie zgłoszenia (np. "Nowe", "W trakcie naprawy", "Zamknięte") pomagają w zarządzaniu procesem naprawy błędów. 
Wymień elementy, z których składa się plan testów. 
lista elementów składających się na plan testów:  
Identyfikator planu testów .
Wprowadzenie .
Testowane elementy .
Testowane cechy/funkcje .
Wyłączenia z zakresu .
Podejście do testowania .
Kryteria zaliczenia/niezaliczenia testu .
Kryteria zawieszenia i wznowienia testowania .
Produkty testowania .
Zadania testowania .
Środowiska testowe .
Odpowiedzialności .
Potrzeby szkoleniowe i zapotrzebowanie na zasoby .
Harmonogram .
Ryzyka i plany awaryjne .
Zatwierdzenie planu .
Podaj różnicę pomiędzy scenariuszem testowym a przypadkiem testowym. 
Scenariusz testowy to ogólny opis funkcjonalności, którą chcemy przetestować, podczas gdy przypadek testowy to konkretny zestaw kroków, danych wejściowych i oczekiwanych wyników, służący do sprawdzenia danej funkcjonalności. Scenariusz testowy określa "co" chcemy przetestować, a przypadek testowy określa "jak" to zrobić, przy czym przypadek testowy jest bardziej szczegółowy i wymaga więcej czasu i zasobów na stworzenie. """

# Funkcja do generowania plików audio
def generate_audio(text, index):
    tts = gTTS(text, lang=lang) 
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
    video_with_subtitle.write_videofile(video_with_subtitle_file, fps=1)
    
    return video_with_subtitle_file

# Funkcja do łączenia plików wideo w całość
def combine_videos(video_files):
    clips = [VideoFileClip(vf) for vf in video_files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("final_video.mp4", fps=1)

# Dzielimy tekst na zdania
sentences = re.split(r'[.!?]', text)
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
