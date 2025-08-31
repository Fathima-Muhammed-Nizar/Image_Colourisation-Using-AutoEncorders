# Overview

This project is a Deep Convolutional Neural Network approach to solve the task of image colorization. The goal is to produce a colored image given a grayscale image.
At it's heart, it uses Convolutional Auto-Encoders to solve this task. First few layers of ResNet-18 model are used as the Encoder, and the Decoder consists of a series of Deconvolution layers (i.e., upsample layers followed by convolutions) and residual connections.
The model is trained on a subset of MIT Places365 dataset, consisting of 41000 images of landscapes and scenes.Given an image, the model can colorize it.   

# Steps to run 

Clone repo  
Create virtual environment  
Install requirements.txt 
Then follow below steps:  
step 1:  
Go to the projects folder

step 2:  
Activate the virtual environment

step 3:    
Execute the command  
python colorize.py -i <path/to/image.jpg> -o <path/to/output.jpg> -r 360  

Note:    
As the model is trained with 224x224 images, it gives best results when --res is set to lower resolutions (<=480) and okay-ish when set around ~720.  
Setting --res higher than that of input image won't increase the output's quality.  

# Results

<img width="778" height="424" alt="Screenshot 2025-08-31 at 2 47 10 PM" src="https://github.com/user-attachments/assets/4ebc2fb7-8b56-41cc-b804-48c89eebd588" />
