import cv2
import numpy as np

# Load an image
image_path = 'D:\\all prac 3\\,\\linear algebra\\final journal la\\abc.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', grayscale_image)
    
    # Resize the image
    new_size = (300, 200)  # Replace with your desired dimensions
    resized_image = cv2.resize(image, new_size)
    cv2.imshow('Resized Image', resized_image)
    
    # Save the resized image
    cv2.imwrite('resized_image.jpg', resized_image)
    
    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
