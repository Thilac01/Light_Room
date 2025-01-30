import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as img
from scipy.ndimage import convolve, gaussian_filter
from matplotlib import colors
import streamlit as st

# Load the image
image = img.imread("pic2.webp")

# Create the Filters class
class Filters:
    def high_pass(self, image):
        hp_kernel = np.array([
            [1, 1, 1],
            [1,  -8, 1],
            [1, 1, 1]
        ])
        filtered_image = np.zeros_like(image, dtype=np.float32)
        for i in range(3): 
            filtered_image[:, :, i] = convolve(image[:, :, i], hp_kernel, mode='constant', cval=0)
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
        return filtered_image

    def low_pass(self, image): 
        lp_kernel = np.array([
            [1, 1, 1],
            [1,  -8, 1],
            [1, 1, 1]
        ])
        filtered_image = np.zeros_like(image, dtype=np.float32)
        for i in range(3): 
            filtered_image[:, :, i] = convolve(image[:, :, i], lp_kernel, mode='constant', cval=0)
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
        return filtered_image

    def brightness(self, image, factor):
        bright_image = image * factor
        bright_image = np.clip(bright_image, 0, 255).astype(np.uint8)
        return bright_image

    def contrast(self, image, factor):
        contrast_image = (image - 127) * factor + 127
        contrast_image = np.clip(contrast_image, 0, 255).astype(np.uint8)
        return contrast_image

    def sharpen(self, image):
        sharpen_kernel = np.array([
            [0, -1, 0],
            [-1, 5,-1],
            [0, -1, 0]
        ])
        sharpened_image = np.zeros_like(image, dtype=np.float32)
        for i in range(3):
            sharpened_image[:, :, i] = convolve(image[:, :, i], sharpen_kernel, mode='constant', cval=0)
        sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)
        return sharpened_image

    def saturation(self, image, factor):
        image_normalized = image / 255.0
        hsv_image = colors.rgb_to_hsv(image_normalized)
        hsv_image[..., 1] *= factor
        hsv_image[..., 1] = np.clip(hsv_image[..., 1], 0, 1)
        rgb_image = colors.hsv_to_rgb(hsv_image)
        return (rgb_image * 255).astype(np.uint8)

    def vignette(self, image, strength=0.5):
        height, width = image.shape[:2]
        y, x = np.ogrid[:height, :width]
        center_x, center_y = width // 2, height // 2
        dist = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        max_dist = np.sqrt(center_x**2 + center_y**2)
        vignette_mask = 1 - (dist / max_dist) * strength
        vignette_mask = np.clip(vignette_mask, 0, 1)
        vignette_image = image * vignette_mask[..., None]
        return np.clip(vignette_image, 0, 255).astype(np.uint8)

    def luminance_noise_reduction(self, image, sigma=1.0):
        # Convert image to luminance (grayscale) for noise reduction
        luminance = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        # Apply Gaussian filter for noise reduction
        smoothed_luminance = gaussian_filter(luminance, sigma=sigma)
        # Replace the luminance in the image with the smoothed luminance
        image[..., 0] = smoothed_luminance
        image[..., 1] = smoothed_luminance
        image[..., 2] = smoothed_luminance
        return np.clip(image, 0, 255).astype(np.uint8)

# Create the Streamlit app layout
st.title("Image Filter Effects with Luminance Noise Reduction")

st.sidebar.header("Adjust Filter Settings")

# Sliders for filter parameters
brightness_factor = st.sidebar.slider("Brightness", 0.0, 2.0, 1.0, 0.1)
contrast_factor = st.sidebar.slider("Contrast", 0.0, 3.0, 1.0, 0.1)
saturation_factor = st.sidebar.slider("Saturation", 0.0, 3.0, 1.0, 0.1)
vignette_strength = st.sidebar.slider("Vignette Strength", 0.0, 1.0, 0.5, 0.1)
luminance_sigma = st.sidebar.slider("Luminance Noise Reduction (Sigma)", 0.0, 3.0, 1.0, 0.1)

# Create a filter object
filter = Filters()

# Apply selected filters
bright_image = filter.brightness(image, brightness_factor)
contrast_image = filter.contrast(image, contrast_factor)
sharpened_image = filter.sharpen(image)
saturated_image = filter.saturation(image, saturation_factor)
vignette_image = filter.vignette(image, vignette_strength)
noise_reduced_image = filter.luminance_noise_reduction(image.copy(), luminance_sigma)

# Display original and filtered images
st.subheader("Original Image")
st.image(image, caption="Original Image", use_column_width=True)

st.subheader("Brightened Image")
st.image(bright_image, caption="Brightened Image", use_column_width=True)

st.subheader("High Contrast Image")
st.image(contrast_image, caption="High Contrast Image", use_column_width=True)

st.subheader("Sharpened Image")
st.image(sharpened_image, caption="Sharpened Image", use_column_width=True)

st.subheader("Saturated Image")
st.image(saturated_image, caption="Saturated Image", use_column_width=True)

st.subheader("Vignette Effect")
st.image(vignette_image, caption="Vignette Effect", use_column_width=True)

st.subheader("Luminance Noise Reduced Image")
st.image(noise_reduced_image, caption="Luminance Noise Reduced Image", use_column_width=True)
