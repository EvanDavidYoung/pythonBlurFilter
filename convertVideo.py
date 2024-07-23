import moviepy.editor as mp
from PIL import ImageFilter, Image
import numpy as np

# Load the video
video_path = "IMG_4354.MOV"
video = mp.VideoFileClip(video_path)

# Define a function to apply horizontal blur (simulating astigmatism) and general blur (bad vision)
def apply_vision_effects(image):
    # Apply horizontal blur
    image = Image.fromarray(image).filter(ImageFilter.GaussianBlur(radius=8))
    # Apply general blur
    image = image.filter(ImageFilter.GaussianBlur(radius=5))
    return np.array(image)

# Apply the effects to each frame of the video
video_with_effects = video.fl_image(apply_vision_effects)

# Ensure the audio is included
video_with_effects = video_with_effects.set_audio(video.audio)

# Save the result
result_video_path = "./astigmatism_bad_vision_effect_video.mp4"
video_with_effects.write_videofile(result_video_path, codec="libx264", fps=video.fps, audio_codec="aac")
