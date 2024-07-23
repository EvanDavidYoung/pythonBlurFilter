import moviepy.editor as mp
from PIL import ImageFilter, Image
import numpy as np
from scipy.ndimage import gaussian_filter
# Load the video
video_path = "IMG_4354.MOV"
video = mp.VideoFileClip(video_path)

# Define a function to apply directional blur (simulating astigmatism)
def apply_vision_effects(image):
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Separate the image into its color channels
    if image_array.ndim == 3:
        channels = [gaussian_filter(image_array[..., i], sigma=(15, 1)) for i in range(image_array.shape[-1])]
        image_blurred = np.stack(channels, axis=-1)
    else:
        image_blurred = gaussian_filter(image_array, sigma=(15, 1))

    # Apply additional general blur to simulate bad vision
    if image_blurred.ndim == 3:
        channels_final = [gaussian_filter(image_blurred[..., i], sigma=5) for i in range(image_blurred.shape[-1])]
        image_final = np.stack(channels_final, axis=-1)
    else:
        image_final = gaussian_filter(image_blurred, sigma=5)
    
    return image_final

# Apply the effects to each frame of the video
video_with_effects = video.fl_image(lambda image: apply_vision_effects(image))

# Ensure the audio is included
video_with_effects = video_with_effects.set_audio(video.audio)

# Save the result with the original frame rate and audio
result_video_path = "astigmatism_bad_vision_effect_video.mp4"
video_with_effects.write_videofile(result_video_path, codec="libx264", fps=video.fps, audio_codec="aac")