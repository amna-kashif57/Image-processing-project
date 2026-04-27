
# Image Processing Transformations in Python

 Overview
This project is a simple interactive image processing tool built in Python. It applies different intensity transformations on grayscale images and visualizes the results side by side with the original image.

The goal of this project is to understand basic image processing techniques and how pixel-level transformations affect image appearance.
 

 Features
This program supports the following image transformations:

- Negative Image Transformation  
- Thresholding (Upward and Downward)  
- Intensity Scaling  
- Logarithmic Transformation  
- Power Law (Gamma Correction)  

Each transformation helps in enhancing or modifying image contrast and brightness in different ways.
 

 How It Works
1. The user provides an image file path.
2. The image is converted into grayscale.
3. The user selects a transformation type.
4. The selected transformation is applied using NumPy operations.
5. The original and processed images are displayed side by side using Matplotlib.

 

 Technologies Used
- Python  
- NumPy (for numerical operations)  
- Matplotlib (for visualization)  
- Scikit-Image (for image reading)  

 Input
- The program reads an image from a local file path:
