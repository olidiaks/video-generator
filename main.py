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

lang = 'en'

text = """
Example is generated by chatgpt to present working of script.
The Importance of Lifelong Learning
In today’s fast-paced, ever-changing world, lifelong learning has become more important than ever. The traditional idea of education as something that happens only in school is outdated. Instead, learning is now viewed as a continuous process that extends throughout our entire lives. This shift is driven by advancements in technology, the changing job market, and the need for personal growth.

One of the key reasons lifelong learning is essential is that technology is rapidly evolving. New developments in fields like artificial intelligence, robotics, and information technology are reshaping industries. To stay relevant and competitive in the job market, individuals must continuously update their skills and knowledge. Employers increasingly value workers who demonstrate adaptability and a willingness to learn new things, making lifelong learning a critical asset for career success.

In addition to professional benefits, lifelong learning plays a crucial role in personal development. It helps us broaden our horizons, become more open-minded, and understand the world in new ways. Whether learning a new language, exploring different cultures, or gaining knowledge about subjects outside of our daily experiences, continuous learning enriches our lives.

Moreover, lifelong learning promotes mental well-being. Studies have shown that keeping the brain active through learning can improve cognitive function, enhance memory, and reduce the risk of dementia in old age. It helps people stay engaged with the world, fostering a sense of purpose and curiosity.

In conclusion, lifelong learning is not just a tool for career advancement but a pathway to personal fulfillment. In a world that is constantly changing, the ability to adapt, grow, and continue learning is crucial. By embracing a mindset of lifelong learning, we equip ourselves to thrive both professionally and personally, no matter what challenges the future may bring.
"""

def generate_audio(text, index):
    tts = gTTS(text, lang=lang) 
    audio_file = f"audio_{index}.mp3"
    tts.save(audio_file)
    return audio_file

def create_video_with_subtitle(audio_file, text, index):
    audio_clip = AudioFileClip(audio_file)
    duration = audio_clip.duration
    
    video_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=duration)
    
    txt_clip = TextClip(text, fontsize=40, color='green', size=video_clip.size, method="caption", print_cmd=True)
    txt_clip = txt_clip.set_position('center').set_duration(duration)
    
    video_with_subtitle = CompositeVideoClip([video_clip, txt_clip]).set_audio(audio_clip)
    
    video_with_subtitle_file = f"video_{index}.mp4"
    video_with_subtitle.write_videofile(video_with_subtitle_file, fps=1)
    
    return video_with_subtitle_file

def combine_videos(video_files):
    clips = [VideoFileClip(vf) for vf in video_files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("final_video.mp4", fps=1)

sentences = re.split(r'[.!?]', text)
audio_files = []
video_files = []

for i, sentence in enumerate(sentences):
    if sentence.strip(): 
        audio_file = generate_audio(sentence.strip(), i)
        audio_files.append(audio_file)
        
        video_file = create_video_with_subtitle(audio_file, sentence.strip(), i)
        video_files.append(video_file)
        
        print(f"Zdanie {i+1}: {sentence.strip()}")


combine_videos(video_files)

for audio_file in audio_files:
    os.remove(audio_file)
for video_file in video_files:
    os.remove(video_file)

print("Wszystkie klipy wideo zostały połączone w 'final_video.mp4'")
