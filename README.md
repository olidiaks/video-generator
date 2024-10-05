# Text-to-Video Generator with Subtitles

This Python project transforms text into engaging video clips, converting each sentence into speech while displaying it as subtitles. The result is a seamless video that plays audio alongside its corresponding text.

To get started with this project, simply fork the repository or download it directly to your machine.

We welcome your suggestions for improvements or features! If you have any ideas, please don’t hesitate to share.

### Contribution Requests

I'm looking for help with the following enhancements:
- **Multithreading:** Improve the program's performance by enabling it to run across multiple threads. I’m currently limited in my Python skills for this task.
- **GUI Development:** Create a user-friendly graphical interface to make the tool more accessible for non-technical users.
- **Cross-Platform Testing:** Verify functionality on Windows and macOS (OS X).

## Installation (Linux, with potential for other OS)

1. Download the repository as a ZIP archive (then unpack it) or clone it using:
   ```bash
   git clone https://github.com/olidiaks/video-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd video-generator
   ```
3. Activate your virtual environment:
   ```bash
   source myenv/bin/activate
   ```
4. Run the main script:
   ```bash
   python main.py
   ```

## Usage Instructions

1. Open `main.py` and change the `lang` variable on line 18 to the language in which the text will be spoken.
2. Modify the `text` variable to include your desired content. Place your text within triple quotes `""" <your text> """`, replacing lines 21 to 31 as needed. Longer speeches are welcome!
3. Execute the following commands:
   ```bash
   source myenv/bin/activate
   python main.py
   ```
   Sit back and wait for your movie to be generated!

## Features

- **Text-to-Speech Conversion:** 
  Utilizes the `gTTS` (Google Text-to-Speech) library to convert input text into audio for each sentence.
  
- **Video Creation with Subtitles:** 
  Generates individual video clips for each sentence, featuring subtitles against a black background while the corresponding audio plays.

- **Video Concatenation:** 
  Merges all video clips into a single, cohesive final video.

- **Automated Cleanup:** 
  Cleans up by deleting temporary audio and video files after the final video is created.

## How It Works

1. **Audio Generation:**  
   Each sentence from the input text is converted into an audio file (`.mp3`) using `gTTS`.

2. **Video Creation:**  
   For every sentence, a video clip is created using `moviepy`, displaying the audio alongside subtitles in the center of the screen.

3. **Video Concatenation:**  
   All individual clips are compiled into one final video file (`final_video.mp4`).

4. **Cleanup:**  
   Temporary audio and video files are automatically removed once the final video is completed.

## Requirements

- Python 3.x
- `gTTS` (`pip install gTTS`)
- `moviepy` (`pip install moviepy`)
