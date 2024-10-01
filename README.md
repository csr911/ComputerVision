# ComputerVision


## Overview

This project focuses on segmenting brain metastases in MRI scans using two advanced architectures: **Nested U-Net** and **Attention U-Net**. Accurate segmentation is crucial for the assessment and treatment of brain tumors.

## Architecture

# Nested U-Net (U-Net++)

Nested U-Net improves upon the traditional U-Net by adding additional skip pathways, which helps in better feature propagation.


# Attention U-Net

Attention U-Net incorporates attention mechanisms to focus on more relevant features, enhancing segmentation performance, especially in complex images.

## Data Preprocessing

# Load Data: Images and their corresponding masks are read from the file system.
# CLAHE: Contrast Limited Adaptive Histogram Equalization (CLAHE) is applied for better contrast.
# Normalization: Pixel values are normalized to the range [0, 1].
# Data Augmentation: Includes rotation, shifting, and flipping to improve model generalization.

## Model Training

Both models are trained using the Adam optimizer with binary cross-entropy loss. The training is monitored using the DICE score, which is crucial for evaluating the performance of segmentation tasks.


## Web Application

A user-friendly web application is built using FastAPI for the backend and Streamlit for the frontend, allowing users to upload MRI images and receive the segmented outputs.


## FastAPI Endpoint

POST /predict/: Upload an MRI image to get segmentation results.

## Streamlit UI

The application allows users to:


Upload a brain MRI image.
View the uploaded image and its segmentation.
View and download the segmentation result.
