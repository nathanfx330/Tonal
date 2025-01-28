# Tonal

⚠️ **Seizure Warning**: The visuals created by this project are based on audio intensity and may include rapid flashes or changes in brightness. Use caution if you are sensitive to flashing lights or have a history of seizures.


**Tonal** transforms audio into captivating visualizations by converting audio intensity into dynamic video frames. Using a logarithmic scale, it translates sound intensity into grayscale values (ranging from 0 to 255), which drive animations in Blackmagic Fusion. This process leverages the Probe modifier to enable seamless integration of audio-driven animations into your creative projects. The tool processes audio files frame by frame, creating engaging visuals that dynamically respond to the sound's energy.
## Features
- Converts audio intensity into video frame values (0 to 1).
- Bakes a Real-time audio visualization using a logarithmic scale.
- Ideal for long-format projects: export the video and use the Probe Modifier in Resolve/Fusion to drive animations.

## Requirements
- Python 3.x
- `pydub` (for audio processing)
- `numpy` (for numerical operations)
- `opencv-python` (for video creation)
- `moviepy` (for video/audio synchronization)
- `ffmpeg` (for video processing)

## Installation

### 1. Clone the Repository:
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/tonal.git
```

### 2. Install Dependencies:
Navigate to the project directory and install required dependencies:

```bash
cd tonal
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install pydub numpy opencv-python moviepy
```

### 3. Install FFmpeg:
Install FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your system’s PATH.

## How to Use

### 1. Run the Script:
Run the script with:

```bash
python tonal.py
```

### 2. Choose an Audio File:
Select an audio file (`.mp3`, `.mp4`, `.mov`, `.avi`) for processing. The script generates a video based on the audio intensity.

### 3. Customizing Segment Length:
Modify the segment length in the `split_video` function (default: 60 seconds), useful for DaVinci Resolve processing.

### 4. Final Output:
The script will output a video (`audio_filename_final.mp4`) with audio visualization and optionally split it into smaller segments.

## Example Usage

```bash
python tonal.py
```

1. Select an audio file.
2. The script generates a video and saves it as `audio_filename_final.mp4`.
3. Split segments are saved in the same directory.

## License
MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [PyDub](https://pydub.com/) for audio processing.
- [OpenCV](https://opencv.org/) for video creation.
- [MoviePy](https://zulko.github.io/moviepy/) for video/audio synchronization.
- [FFmpeg](https://ffmpeg.org/) for video format conversion.
- [NumPy](https://numpy.org/) for numerical computations.
```
