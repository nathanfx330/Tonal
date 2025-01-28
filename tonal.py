import os
import numpy as np
from pydub import AudioSegment
import cv2  # Import OpenCV
from moviepy.editor import VideoFileClip, AudioFileClip

def list_media_files(directory):
    extensions = ['.mp3', '.mp4', '.mov', '.avi']
    files = [file for file in os.listdir(directory) if any(file.endswith(ext) for ext in extensions)]
    return files

def logarithmic_scale(intensity, max_intensity):
    if intensity == 0:
        return 0
    return np.log1p(intensity) / np.log1p(max_intensity)

def process_audio_with_pydub(audio_path, fps):
    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_channels(1)
    samples = np.array(audio.get_array_of_samples())
    sr = audio.frame_rate

    chunk_size = int(sr / fps)
    num_frames = int(len(samples) / chunk_size)

    video_path = os.path.splitext(audio_path)[0] + "_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_path, fourcc, fps, (30, 30))

    frame_intensities = []
    recent_intensities = []

    for i in range(num_frames):
        start = i * chunk_size
        end = start + chunk_size
        chunk = samples[start:end]
        intensity = np.sqrt(np.mean(chunk**2)) if np.any(chunk) else 0
        frame_intensities.append(intensity)
        recent_intensities.append(intensity)
        if len(recent_intensities) > 4:
            recent_intensities.pop(0)

        average_intensity = np.mean(recent_intensities)
        normalized_intensity = logarithmic_scale(average_intensity, max(frame_intensities))
        frame = create_frame(normalized_intensity, 30, 30)
        video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    video_writer.release()
    return video_path, audio_path

def create_frame(intensity, width, height):
    # Ensure there's always a minimum intensity to avoid black frames
    min_intensity = 0.1  # Adjust this value to set the minimum brightness
    intensity_value = int((np.nan_to_num(intensity) + min_intensity) * 255)
    intensity_value = min(intensity_value, 255)  # Ensure it doesn't exceed max value for RGB
    return np.full((height, width, 3), intensity_value, dtype=np.uint8)

def add_audio_to_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

def main(directory="."):
    files = list_media_files(directory)
    if not files:
        print("No suitable media files found.")
        return

    print("Available files:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")

    selection = int(input("Select a file number to process: ")) - 1
    if selection < 0 or selection >= len(files):
        print("Invalid file selection.")
        return

    audio_path = os.path.join(directory, files[selection])
    fps = 30 
    video_path, audio_path = process_audio_with_pydub(audio_path, fps)
    output_video = os.path.splitext(audio_path)[0] + "_final.mp4"
    add_audio_to_video(video_path, audio_path, output_video)
    print("Video with audio created successfully at:", output_video)

if __name__ == '__main__':
    main()

