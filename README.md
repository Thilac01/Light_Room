# Image Filter Effects with Luminance Noise Reduction

This Streamlit application allows users to apply different image filters to enhance and modify their images. It includes filters such as brightness, contrast, saturation, sharpening, vignette effect, and luminance noise reduction. The app provides sliders to adjust each filter's parameters for fine-grained control.

## Features:
- **Brightness Adjustment**: Increases or decreases the brightness of the image.
- **Contrast Adjustment**: Enhances or reduces the contrast of the image.
- **Saturation Adjustment**: Increases or decreases the saturation, enhancing the colors.
- **Sharpening**: Applies a sharpening filter to make the image crisper.
- **Vignette Effect**: Adds a vignette effect that darkens the corners of the image.
- **Luminance Noise Reduction**: Reduces noise based on luminance using a Gaussian filter.

## Filters and the Math Behind Them:

### 1. **Brightness**
   - **Mathematics**: The brightness filter works by multiplying each pixel value by a constant factor:
     $$
     I' = I \times \text{factor}
     $$
     where \( I \) is the original pixel value and \( I' \) is the adjusted pixel value.

### 2. **Contrast**
   - **Mathematics**: Contrast adjustment stretches the difference between pixel values from the mean. The adjustment is given by:
     $$
     I' = (\text{factor} \times (I - 127)) + 127
     $$
     where \( I \) is the original pixel value and \( I' \) is the resulting pixel value after applying contrast.

### 3. **Saturation**
   - **Mathematics**: Saturation is adjusted by modifying the saturation channel in the HSV (Hue, Saturation, Value) color space:
     $$
     S' = S \times \text{factor}
     $$
     where \( S \) is the saturation component of the HSV representation of the image.

### 4. **Sharpening**
   - **Mathematics**: Sharpening is applied by convolving the image with a kernel that emphasizes edges:
     $$
     \text{Kernel} =
     \begin{bmatrix}
     0 & -1 & 0 \\
     -1 & 5 & -1 \\
     0 & -1 & 0
     \end{bmatrix}
     $$
     The sharpening kernel enhances edges by subtracting the surrounding pixels' values and adding a factor to the center pixel.

### 5. **Vignette**
   - **Mathematics**: The vignette effect darkens the corners of the image based on the distance from the center:
     $$
     M(x, y) = 1 - \left(\frac{d(x, y)}{d_{\text{max}}}\right) \times \text{strength}
     $$
     where \( d(x, y) \) is the distance of a pixel from the center and \( d_{\text{max}} \) is the maximum distance from the center to the corners.

### 6. **Luminance Noise Reduction**
   - **Mathematics**: Luminance noise reduction starts by converting the image to grayscale (luminance), then applying a Gaussian filter to smooth the luminance channel:
     $$
     I_{\text{luminance}} = 0.2989 \times R + 0.5870 \times G + 0.1140 \times B
     $$
     where \( R \), \( G \), and \( B \) are the red, green, and blue channels. A Gaussian filter is applied to reduce noise:
     $$
     I'_{\text{luminance}} = \text{GaussianFilter}(I_{\text{luminance}}, \sigma)
     $$

## Usage

1. **Install Dependencies**:
   To run this application, you need to install the dependencies listed in the `requirements.txt` file. You can install them by running:
   ```bash
   pip install -r requirements.txt
![Screenshot 2025-01-30 082534](https://github.com/user-attachments/assets/fedb6a80-e6d1-4d05-9740-daf98d9bbe32)
![Screenshot 2025-01-30 082607](https://github.com/user-attachments/assets/7b91fc11-fcd9-4323-b0fb-ff50d22cc8c0)

