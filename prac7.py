import cv2
import numpy as np

# Load two images for addition, multiplication, and subtraction
image1 = cv2.imread('D:\\all prac 3\\,\\linear algebra\\final journal la\\xyz.jpg')  # Replace with your image path
image2 = cv2.imread('D:\\all prac 3\\,\\linear algebra\\final journal la\\lmn.jpg')  # Replace with your image path

# Check if the images were loaded successfully
if image1 is None or image2 is None:
    print("Error: Unable to load one or both of the images.")
else:
    # Display the original images
    cv2.imshow('Image 1', image1)
    cv2.imshow('Image 2', image2)
    
    # Ensure both images have the same dimensions
    if image1.shape == image2.shape:
        # Perform addition
        addition_result = cv2.add(image1, image2)
        cv2.imshow('Image Addition', addition_result)
        
        # Perform subtraction
        subtraction_result = cv2.subtract(image1, image2)
        cv2.imshow('Image Subtraction', subtraction_result)
        
        # Perform multiplication
        multiplication_result = cv2.multiply(image1, image2)
        cv2.imshow('Image Multiplication', multiplication_result)
        
        # Wait for a key press and then close all windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Images must have the same dimensions for addition and subtraction.")
