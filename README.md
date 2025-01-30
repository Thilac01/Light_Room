# Image Filter Effects with Luminance Noise Reduction

This Streamlit application allows users to apply different image filters to enhance and modify their images. It includes filters such as brightness, contrast, saturation, sharpening, vignette effect, and luminance noise reduction. The app is designed to give users control over each filter's parameters through sliders for fine-grained adjustments.

## Features:
- **Brightness Adjustment**: Increases or decreases the brightness of the image.
- **Contrast Adjustment**: Enhances or reduces the contrast of the image.
- **Saturation Adjustment**: Increases or decreases the saturation, enhancing the colors.
- **Sharpening**: Applies a sharpening filter to make the image crisper.
- **Vignette Effect**: Adds a vignette effect that darkens the corners of the image.
- **Luminance Noise Reduction**: Reduces noise based on luminance using a Gaussian filter.

## Filters and the Math Behind Them:

### 1. **Brightness**
   - **Mathematics**: The brightness filter is applied by multiplying each pixel value by a constant factor:
     \[
     I' = I \times \text{factor}
     \]
     where \(I\) is the original pixel value and \(I'\) is the resulting pixel value after adjustment.

### 2. **Contrast**
   - **Mathematics**: Contrast is enhanced by stretching the difference between pixel values from the mean. The adjustment is given by:
     \[
     I' = (\text{factor} \times (I - 127)) + 127
     \]
     where \(I\) is the original pixel value, and \(I'\) is the resulting pixel value after applying contrast.

### 3. **Saturation**
   - **Mathematics**: The saturation filter works in the HSV (Hue, Saturation, Value) color space. It multiplies the saturation channel (S) by a factor:
     \[
     S' = S \times \text{factor}
     \]
     where \(S\) is the saturation channel of the HSV color representation of the image.

### 4. **Sharpening**
   - **Mathematics**: A sharpening filter is applied by convolving the image with a kernel that emphasizes the center pixel, enhancing edges:
     \[
     \text{Kernel} =
     \begin{bmatrix}
     0 & -1 & 0 \\
     -1 & 5 & -1 \\
     0 & -1 & 0
     \end{bmatrix}
     \]
     This kernel enhances edges by subtracting the surrounding pixels' values and adding a factor to the center pixel.

### 5. **Vignette**
   - **Mathematics**: The vignette effect is achieved by applying a mask based on the distance of each pixel from the center of the image:
     \[
     M(x, y) = 1 - \left(\frac{d(x, y)}{d_{\text{max}}}\right) \times \text{strength}
     \]
     where \(d(x, y)\) is the distance of a pixel from the center, and \(d_{\text{max}}\) is the maximum possible distance. The mask is applied to each pixel, darkening the corners of the image.

### 6. **Luminance Noise Reduction**
   - **Mathematics**: Luminance noise reduction is achieved by first converting the image to grayscale (luminance), then applying a Gaussian filter to smooth the image:
     \[
     I_{\text{luminance}} = 0.2989 \times R + 0.5870 \times G + 0.1140 \times B
     \]
     where \(R\), \(G\), and \(B\) are the red, green, and blue channels of the image. A Gaussian filter is then applied to the luminance channel to reduce noise:
     \[
     I'_{\text{luminance}} = \text{GaussianFilter}(I_{\text{luminance}}, \sigma)
     \]
     The smoothed luminance is then mapped back to the color channels of the image.

## Usage

1. **Install Dependencies**:
   To run this application, you need to install the following dependencies:
   ```bash
   pip install numpy matplotlib scipy streamlit
