Here’s an updated `README.md` for your **Tonal** project with the changes you requested. This version includes more detailed explanations of how **Tonal** works with DaVinci Resolve, as well as instructions on using the Fusion Probe Modifier. I've also fixed a few minor things for clarity.

```markdown
# Tonal

**Tonal** transforms audio into dynamic visuals by creating videos based on audio intensity. Using a logarithmic scale, it visualizes sound in real-time, creating engaging video representations. Perfect for audio-visual projects, and optimized for easy processing in DaVinci Resolve/Fusion Probe Modifier.

## Features
- Transforms audio into visual representations using audio intensity.
- Creates a video visualization based on the audio's dynamic range.
- Ideal for long-format video projects. Simply place the exported video in a track, create a Fusion script from it, use the Probe Modifier to sample the video, and drive animation in your script.
- Optimized for DaVinci Resolve/Fusion Probe Modifier for video editing.

## Requirements
- Python 3.x
- `pydub` library (for audio processing)
- `numpy` library (for numerical operations)
- `opencv-python` library (for video creation)
- `moviepy` library (for video/audio synchronization)
- `ffmpeg` (for video processing)

## Installation

### 1. Clone the Repository:
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/tonal.git
```

### 2. Install Dependencies:
Navigate into the project directory and install the required Python dependencies:

```bash
cd tonal
pip install -r requirements.txt
```

Or manually install the dependencies:

```bash
pip install pydub numpy opencv-python moviepy
```

### 3. Install FFmpeg:
Make sure you have `ffmpeg` installed on your system. You can download it from [FFmpeg.org](https://ffmpeg.org/download.html). Once downloaded, make sure `ffmpeg` is added to your system’s PATH.

## How to Use

### 1. Run the Script:
To use **Tonal**, simply run the script with the following command:

```bash
python tonal.py
```

### 2. Choose an Audio File:
The script will prompt you to select an audio file from the supported formats (`.mp3`, `.mp4`, `.mov`, `.avi`). Once you select the file, the script will process it and generate a video based on the audio intensity.

### 3. Customizing Segment Length:
You can customize the segment length for video splits in the `split_video` function, which is particularly useful for processing videos in DaVinci Resolve. The default segment length is set to 60 seconds.

### 4. Final Output:
After processing, the script will output a video file with the audio visualization and optionally split the video into smaller segments for easier editing.

## Example Usage

```bash
python tonal.py
```

1. Select an audio file to visualize.
2. The script will generate a video and save it as `audio_filename_final.mp4`.
3. If enabled, the video will be split into smaller segments and saved in the same directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [PyDub](https://pydub.com/) for audio processing.
- [OpenCV](https://opencv.org/) for video creation.
- [MoviePy](https://zulko.github.io/moviepy/) for video/audio synchronization.
- [FFmpeg](https://ffmpeg.org/) for video format conversion and processing.
- [NumPy](https://numpy.org/) for numerical computations.

```

### Additional Notes:

- **Fusion Probe Modifier**: As you mentioned, the visualizations from **Tonal** are particularly useful in DaVinci Resolve with the **Fusion Probe Modifier**. This functionality allows you to apply the audio-driven animation to video layers and tracks within DaVinci Resolve by extracting and using the video data from the generated output.

- **Final Output**: After running the script, the resulting video can be used for further editing and animation within DaVinci Resolve, with dynamic changes driven by the audio's intensity data.

---

This **README.md** should be a comprehensive guide to getting started with your project! Let me know if you need any more tweaks. 😊
