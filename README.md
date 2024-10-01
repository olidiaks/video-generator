# Text-to-Video Generator with Subtitles

This Python project converts text into video clips, with each sentence transformed into speech and displayed as subtitles. The final output is a concatenated video file that plays audio and displays subtitles for each sentence.

If you'd like to suggest any changes or improvements to the project, feel free to do so!

If anyone knows how to achieve this, it would be greatly appreciated:
* Make the program work across multiple threads. My Python skills are a bit limited for that at the moment.

## Features

- **Text-to-Speech Conversion:** 
  Converts each sentence from the input text into audio using the `gTTS` (Google Text-to-Speech) library.
  
- **Video Creation with Subtitles:** 
  Creates a video clip for each sentence, displaying the sentence as a subtitle on a black background while the audio is played.

- **Concatenation of Video Clips:** 
  Combines all the individual video clips into one final video.

- **Automated Cleanup:** 
  Deletes all temporary audio and video files after generating the final video.

## How It Works

1. **Audio Generation:**  
   Each sentence from the input text is converted into an audio file (`.mp3`) using `gTTS`.

2. **Video Creation:**  
   For each sentence, a video clip is generated using `moviepy`, where the audio is played and the sentence appears as a subtitle in the center of the screen.

3. **Video Concatenation:**  
   All individual video clips are combined into a single video file (`final_video.mp4`).

4. **Cleanup:**  
   After the final video is created, temporary files (both audio and video) are removed.

## Requirements

- Python 3.x
- `gTTS` (`pip install gTTS`)
- `moviepy` (`pip install moviepy`)
