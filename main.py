#!/bin/python3

import cv2
from gtts import gTTS
import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip

audio_language = 'en'
# Example usage
text_lines = ["Hello World!", "Welcome to OpenCV.", "This is dynamic text.", "Enjoy your video!"]
audio_file = "voice_over.mp3"
video_file = 'sample_vid.mp4'

# Function to create audio from text
def create_audio(text_lines, audio_file, lang):
    combined_audio = ""
    for line in text_lines:
        tts = gTTS(text=line, lang=lang)
        tts.save(f"{line}.mp3")
        combined_audio += f"{line}.mp3 "
    
    # Combine all audio files into one using MoviePy
    audio_clips = [AudioFileClip(f"{line}.mp3") for line in text_lines]
    final_audio = concatenate_audioclips(audio_clips)
    final_audio.write_audiofile(audio_file)

    # Clean up temporary audio files
    for line in text_lines:
        os.remove(f"{line}.mp3")

# Function to create video with dynamic text
def create_video_with_text(video_path, text_lines, audio_file):
    cap = cv2.VideoCapture(video_path)
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_number = 0

    # Prepare the output video
    output_frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Update the text based on the current frame number
        on_video_text = text_update(frame_number // fps, text_lines)

        # Define font and position for the text
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (50, 50)  # Position of the text on the frame
        color = (0, 255, 255)  # Yellow color in BGR format
        thickness = 2
        
        # Put text on the video frame
        cv2.putText(frame, on_video_text, position, font, 1, color, thickness, cv2.LINE_AA)

        # Append frame to output list
        output_frames.append(frame)

        frame_number += 1

    cap.release()

    # Create a video clip from frames and add audio
    height, width, layers = output_frames[0].shape
    out_video = VideoFileClip(video_path).subclip(0, len(output_frames) / fps)
    
    final_video = CompositeVideoClip([out_video.set_duration(len(output_frames) / fps)])
    
    # Set audio to the final video
    final_audio = AudioFileClip(audio_file)
    final_video.set_audio(final_audio)
    
    final_video.write_videofile("output_video.mp4", codec="libx264")

# Function to update text based on the current frame
def text_update(frame_number, text_lines):
    if frame_number < len(text_lines):
        return text_lines[frame_number]
    else:
        return "End of Text"


# Create audio from text lines
create_audio(text_lines, audio_file, audio_language)

# Create video with dynamic text and voice over
create_video_with_text(video_file, text_lines, audio_file)
