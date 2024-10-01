# Computer Vision

# Brain MRI Metastasis Segmentation

This project focuses on segmenting brain metastases in MRI scans using two advanced architectures: **Nested U-Net** and **Attention U-Net**. Accurate segmentation of brain metastases is crucial for clinical decision-making and treatment planning. This document provides a comprehensive overview of the project, best practices for setup and execution, architecture explanations, challenges faced, and a video demonstration of the Streamlit UI.

## Architectures

### 1.1 Nested U-Net (U-Net++):
Nested U-Net, also known as U-Net++, extends the traditional U-Net architecture by introducing nested skip pathways. This enhances feature propagation and allows for better gradient flow throughout the network, ultimately leading to improved segmentation performance. The multiple nested skip connections ensure that high-resolution features from the encoder are effectively utilized in the decoder, allowing the model to capture intricate details in the MRI scans. 

### 1.2 Attention U-Net:
Attention U-Net incorporates attention mechanisms into the U-Net architecture, enabling the model to focus on the most relevant regions during segmentation. By adding attention gates, the model can differentiate between important features and background noise. This is especially beneficial in medical imaging, where the presence of noise or irrelevant structures can mislead segmentation results. The attention mechanism refines the learning process, resulting in more precise and clinically relevant segmentations.

## Data Preprocessing

1. **Load Data**: Images and their corresponding masks are read from the file system.
2. **CLAHE**: Contrast Limited Adaptive Histogram Equalization (CLAHE) is applied for better contrast.
3. **Normalization**: Pixel values are normalized to the range [0, 1].
4. **Data Augmentation**: Includes rotation, shifting, and flipping to improve model generalization.

## Model Training

Both models are trained using the Adam optimizer with binary cross-entropy loss. The training is monitored using the DICE score, which is crucial for evaluating the performance of segmentation tasks.

## Web Application

A user-friendly web application is built using **FastAPI** for the backend and **Streamlit** for the frontend, allowing users to upload MRI images and receive the segmented outputs.

### FastAPI Endpoint

- **POST /predict/**: Upload an MRI image to get segmentation results.

### Streamlit UI

The application allows users to:

- Upload a brain MRI image.
- View the uploaded image and its segmentation.
- View and download the segmentation result.

